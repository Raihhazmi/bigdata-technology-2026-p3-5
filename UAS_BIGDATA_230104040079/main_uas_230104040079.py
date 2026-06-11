import os
import random
from datetime import datetime, timedelta
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, window, hour, sum as _sum

# Inisialisasi Spark Session
spark = SparkSession.builder \
    .appName("UAS_SmartEnergy_230104040079") \
    .getOrCreate()

# ==========================================
# 1. GENERATE DATA
# ==========================================
sectors = ["Industrial A", "Industrial_B", "Residential_C"] # [cite: 55, 56, 57]
data = []
start_time = datetime.now()

# Membuat data per menit untuk masing-masing sektor selama 150 menit [cite: 59]
for i in range(150):
    current_time = start_time + timedelta(minutes=i)
    for sector in sectors:
        power_usage = random.randint(100, 1000) # konsumsi random 100-1000 kWh [cite: 60]
        data.append((current_time, sector, power_usage))

# Buat Spark DataFrame dengan field: timestamp, sector, power_usage [cite: 51, 52, 53]
columns = ["timestamp", "sector", "power_usage"]
df = spark.createDataFrame(data, columns)

# ==========================================
# 2. SPARK PROCESSING
# ==========================================
# 1. Total konsumsi energi per sektor [cite: 63]
df_total_sector = df.groupBy("sector").agg(_sum("power_usage").alias("total_power_usage"))

# 2. Agregasi konsumsi tiap 10 menit [cite: 64]
df_time_10m = df.groupBy(
    window("timestamp", "10 minutes"),
    "sector"
).agg(_sum("power_usage").alias("power_usage_10m"))

# 3. Dataset AI berdasarkan hour (jam) [cite: 65]
df_ml_data = df.withColumn("hour", hour("timestamp")) \
    .groupBy("hour") \
    .agg(_sum("power_usage").alias("total_power_usage"))

# ==========================================
# 3. SIMPAN KE PARQUET (ABSOLUTE PATH)
# ==========================================
# os.path.abspath otomatis mengambil lokasi absolut dari script ini berjalan [cite: 144]
base_dir = os.path.abspath(os.path.dirname(__file__))

# Menentukan folder output 
path_total = os.path.join(base_dir, "output", "energy_total")
path_time = os.path.join(base_dir, "output", "energy_time")
path_ml = os.path.join(base_dir, "output", "ml_energy")

# Save format parquet dengan mode overwrite (agar tidak error kalau di-run ulang)
df_total_sector.write.mode("overwrite").parquet(path_total)
df_time_10m.write.mode("overwrite").parquet(path_time)
df_ml_data.write.mode("overwrite").parquet(path_ml)

print("✅ Data processing sukses! File Parquet berhasil di-generate di folder output/")
spark.stop()