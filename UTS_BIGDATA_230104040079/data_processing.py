import os
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType
from datetime import datetime, timedelta
import random
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Initialize Spark
spark = SparkSession.builder.appName("SmartCampusAnalytics").getOrCreate()

# --- 1. GENERATE DATA ---
buildings = ['Fakultas Sains dan Teknologi', 'Perpustakaan', 'Auditorium']
start_time = datetime.now()
data = []

for i in range(100): # 100 data points
    timestamp = start_time + timedelta(minutes=i)
    building = random.choice(buildings)
    count = random.randint(20, 300)
    data.append((timestamp, building, count))

schema = StructType([
    StructField("timestamp", TimestampType(), True),
    StructField("building", StringType(), True),
    StructField("attendance_count", IntegerType(), True)
])

df = spark.createDataFrame(data, schema)

# --- 2. TRANSFORMATION ---
# a. Total per Gedung
total_per_building = df.groupBy("building").agg(F.sum("attendance_count").alias("total_mahasiswa"))

# b. Tren per 20 Menit
tren_20_menit = df.groupBy(F.window("timestamp", "20 minutes"), "building") \
                  .agg(F.avg("attendance_count").alias("avg_attendance"))

# c. Dataset AI (Ekstrak Jam)
df_ml = df.withColumn("hour", F.hour("timestamp"))
ml_data = df_ml.select("hour", "attendance_count")

# --- 3. STORAGE (PARQUET) ---
output_path = "output/"
total_per_building.write.mode("overwrite").parquet(output_path + "attendance_total")
tren_20_menit.write.mode("overwrite").parquet(output_path + "attendance_time")
df_ml.write.mode("overwrite").parquet(output_path + "ml_attendance")

print("✅ Data Parquet berhasil disimpan di folder output/")

# --- 4. MACHINE LEARNING ---
# Convert to Pandas for Scikit-Learn
pdf = df_ml.select("hour", "attendance_count").toPandas()
X = pdf[['hour']]
y = pdf['attendance_count']

model = LinearRegression()
model.fit(X, y)

# Save Model for Streamlit
joblib.dump(model, 'model_kepadatan.pkl')
print("✅ Model ML berhasil dilatih dan disimpan!")