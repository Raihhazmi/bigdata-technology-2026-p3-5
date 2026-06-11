import streamlit as st
import pandas as pd
import plotly.express as px
import os
from sklearn.linear_model import LinearRegression

# Setup halaman Dashboard
st.set_page_config(page_title="Smart Energy Dashboard", layout="wide")

# ==========================================
# 1. LOAD DATA PARQUET (ABSOLUTE PATH)
# ==========================================
base_dir = os.path.abspath(os.path.dirname(__file__))
path_total = os.path.join(base_dir, "output", "energy_total")
path_time = os.path.join(base_dir, "output", "energy_time")
path_ml = os.path.join(base_dir, "output", "ml_energy")

@st.cache_data
def load_data():
    df_total = pd.read_parquet(path_total)
    df_time = pd.read_parquet(path_time)
    df_ml = pd.read_parquet(path_ml)
    
    # Ekstrak waktu mulai dari kolom window (karena formatnya struct/dict dari Spark)
    df_time['timestamp'] = df_time['window'].apply(lambda x: x['start'] if isinstance(x, dict) else x)
    df_time = df_time.sort_values('timestamp')
    
    return df_total, df_time, df_ml

try:
    df_total, df_time, df_ml = load_data()
except Exception as e:
    st.error(f"Gagal memuat data Parquet. Pastikan file ada di folder output. Error: {e}")
    st.stop()

st.title("⚡ Smart Energy Consumption Analytics")
st.markdown("Dashboard Monitoring dan AI Prediksi Konsumsi Energi Kawasan Industri")

# ==========================================
# 2. KPI & FILTER DROP-DOWN SEKTOR
# ==========================================
col1, col2 = st.columns([1, 3])

with col1:
    st.subheader("Filter Data")
    sektor_list = df_time['sector'].unique().tolist()
    sektor_list.insert(0, "Semua Sektor")
    selected_sector = st.selectbox("Pilih Sektor:", sektor_list)

# Logika Filter
if selected_sector == "Semua Sektor":
    filtered_time = df_time.groupby('timestamp').agg({'power_usage_10m':'sum'}).reset_index()
    total_kpi = df_total['total_power_usage'].sum()
else:
    filtered_time = df_time[df_time['sector'] == selected_sector]
    total_kpi = df_total[df_total['sector'] == selected_sector]['total_power_usage'].sum()

with col2:
    st.subheader("KPI Total Konsumsi Energi")
    st.metric(label=f"Total Konsumsi ({selected_sector})", value=f"{total_kpi:,.0f} kWh")

# ==========================================
# 3. GRAFIK LINE PLOTLY (TREN KONSUMSI)
# ==========================================
st.subheader("📈 Tren Konsumsi Energi (per 10 Menit)")
fig_line = px.line(
    filtered_time, 
    x="timestamp", 
    y="power_usage_10m",
    markers=True,
    title=f"Tren Konsumsi Energi - {selected_sector}",
    labels={"timestamp": "Waktu", "power_usage_10m": "Konsumsi (kWh)"}
)
st.plotly_chart(fig_line, use_container_width=True)

# ==========================================
# 4. MACHINE LEARNING (LINEAR REGRESSION) & ANALISIS
# ==========================================
st.markdown("---")
st.header("🤖 AI Forecasting: Prediksi Konsumsi per Jam")

# Preprocessing data untuk ML
df_ml_clean = df_ml.dropna(subset=['hour', 'total_power_usage']).sort_values('hour')
X = df_ml_clean[['hour']]
y = df_ml_clean['total_power_usage']

# Train Model
model = LinearRegression()
if not X.empty:
    model.fit(X.values, y.values) # Menggunakan .values agar tidak ada warning feature names
    
    col_ml1, col_ml2 = st.columns(2)
    
    with col_ml1:
        st.subheader("Input Prediksi")
        input_hour = st.slider("Pilih Jam Prediksi (0-23):", min_value=0, max_value=23, value=12)
        
        # Eksekusi Prediksi
        pred_value = model.predict([[input_hour]])[0]
        st.info(f"**Prediksi Konsumsi Energi pada Pukul {input_hour:02d}:00 adalah:** \n### {pred_value:,.2f} kWh")
        
    with col_ml2:
        st.subheader("Analisis Jam Tertinggi")
        # Mencari jam dengan konsumsi tertinggi dari data aktual
        max_hour_row = df_ml_clean.loc[df_ml_clean['total_power_usage'].idxmax()]
        max_hour = int(max_hour_row['hour'])
        max_usage = max_hour_row['total_power_usage']
        
        st.success(f"📌 **Insight Analisis:**\n\nBerdasarkan agregasi data AI, konsumsi energi **tertinggi** terjadi pada pukul **{max_hour:02d}:00** dengan total beban **{max_usage:,.0f} kWh**.")
        st.write("Informasi ini sangat berguna bagi perusahaan listrik untuk mengantisipasi lonjakan beban daya dan mencegah pemadaman (overload) pada jam-jam sibuk tersebut.")
else:
    st.warning("Data AI belum memadai untuk training model.")