import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import joblib

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Smart Campus Analytics", 
    page_icon="🏢", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS ---
# Menambahkan styling agar KPI terlihat seperti card modern & minimalis
st.markdown("""
<style>
    div[data-testid="metric-container"] {
        background-color: #f8f9fa;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #e9ecef;
        box-shadow: 2px 4px 12px rgba(0,0,0,0.05);
        transition: transform 0.2s;
    }
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
    }
    @media (prefers-color-scheme: dark) {
        div[data-testid="metric-container"] {
            background-color: #1e1e1e;
            border: 1px solid #333;
            box-shadow: 2px 4px 12px rgba(255,255,255,0.02);
        }
    }
    .main-header {
        font-weight: 700;
        font-size: 2.5rem;
        margin-bottom: -10px;
    }
    .sub-header {
        color: #6c757d;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="main-header">🏢 Smart Campus Attendance Analytics</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Analisis komprehensif kepadatan gedung berdasarkan data <i>tapping</i> kartu mahasiswa.</p>', unsafe_allow_html=True)

# --- LOAD DATA ---
@st.cache_data
def load_data():
    df_total = pd.read_parquet("output/attendance_total")
    df_trend = pd.read_parquet("output/attendance_time")
    
    # PERBAIKAN BUG SUMBU X: Konversi dictionary window menjadi format jam yang bisa dibaca
    df_trend['time_label'] = pd.to_datetime(df_trend['window'].apply(lambda x: x['start'])).dt.strftime('%H:%M')
    
    # Sortir berdasarkan waktu agar garis chart tidak berantakan
    df_trend = df_trend.sort_values(by='time_label')
    return df_total, df_trend

df_total, df_trend = load_data()
model = joblib.load('model_kepadatan.pkl')

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/8074/8074805.png", width=80)
    st.header("⚙️ Filter & Kontrol")
    
    selected_building = st.multiselect(
        "Pilih Gedung:", 
        options=df_total['building'].unique(),
        default=df_total['building'].unique()
    )
    
    st.divider()
    st.subheader("🤖 Engine Prediksi")
    hour_to_predict = st.slider("Pilih Jam Operasional (0-23):", 0, 23, 10)

# --- KPI SECTION ---
st.markdown("### 📊 Key Performance Indicators (Total)")
cols = st.columns(len(selected_building) if len(selected_building) > 0 else 1)
filtered_total = df_total[df_total['building'].isin(selected_building)]

if not filtered_total.empty:
    for i, row in enumerate(filtered_total.itertuples()):
        with cols[i]:
            st.metric(label=f"📍 {row.building}", value=f"{row.total_mahasiswa:,} Mhs")
else:
    st.warning("Silakan pilih minimal satu gedung di sidebar.")

st.write("") # Spacing

# --- CHART SECTION ---
st.markdown("### 📈 Tren Kehadiran Real-time (Interval 20 Menit)")
filtered_trend = df_trend[df_trend['building'].isin(selected_building)]

if not filtered_trend.empty:
    fig_line = px.line(
        filtered_trend, 
        x='time_label', 
        y='avg_attendance', 
        color='building',
        markers=True,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    
    # Styling chart agar lebih modern
    fig_line.update_traces(line_shape='spline', line=dict(width=3), marker=dict(size=8))
    fig_line.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(title="Waktu", showgrid=False, zeroline=False),
        yaxis=dict(title="Rata-rata Mahasiswa", gridcolor='#e0e0e0', zeroline=False),
        hovermode="x unified",
        legend_title="Gedung",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_line, use_container_width=True)

# --- ML PREDICTION SECTION ---
st.divider()
st.markdown("### 🔮 Prediksi Kepadatan Kampus")

# Melakukan prediksi
prediction = model.predict([[hour_to_predict]])
estimasi = int(prediction[0])

col_ml1, col_ml2 = st.columns([1, 2])

with col_ml1:
    # Gauge Chart untuk Prediksi
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = estimasi,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': f"Estimasi Jam {hour_to_predict}:00", 'font': {'size': 16}},
        gauge = {
            'axis': {'range': [0, 400], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#4C78A8"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 100], 'color': '#E8F0FE'},
                {'range': [100, 250], 'color': '#AEC7E8'},
                {'range': [250, 400], 'color': '#FFB5B8'}
            ]
        }
    ))
    fig_gauge.update_layout(height=250, margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig_gauge, use_container_width=True)

with col_ml2:
    st.write("")
    st.write("")
    st.info(f"""
    **Insight Otomatis:**
    Berdasarkan model *Linear Regression*, diperkirakan akan ada sekitar **{estimasi} mahasiswa** yang memadati area kampus pada pukul **{hour_to_predict:02d}:00**.
    """)
    
    # Simple logic untuk status kepadatan
    if estimasi > 250:
        st.error("🚨 **Status:** Kepadatan Tinggi. Direkomendasikan untuk memaksimalkan sirkulasi udara (AC) dan kebersihan fasilitas sanitasi.")
    elif estimasi > 100:
        st.warning("⚠️ **Status:** Kepadatan Sedang. Aktivitas kampus berjalan normal.")
    else:
        st.success("✅ **Status:** Kepadatan Rendah. Area kampus relatif sepi.")