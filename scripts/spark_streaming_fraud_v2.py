from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Inisialisasi Spark Session
spark = SparkSession.builder.appName("FraudDetection").getOrCreate()

# Membaca stream dari Kafka
df_kafka = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "bank_topic") \
    .load()

# Mendefinisikan schema untuk data JSON
schema = StructType([
    StructField("nama", StringType()),
    StructField("rekening", StringType()),
    StructField("jumlah", IntegerType()),
    StructField("lokasi", StringType())
])

# Mengubah value dari Kafka (binary) menjadi string JSON, lalu mengaplikasikan schema
df = df_kafka.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Masking: Menyembunyikan nomor rekening (menyisakan 2 digit terakhir)
df = df.withColumn("rekening_masked",
                   concat(lit("****"), col("rekening").substr(-2, 2)))

# Fraud detection: Memberi label "FRAUD" jika jumlah > 50 juta ATAU lokasi Luar Negeri
df = df.withColumn("status",
                   when(col("jumlah") > 50000000, "FRAUD")
                   .when(col("lokasi") == "Luar Negeri", "FRAUD")
                   .otherwise("NORMAL"))

# Encryption: Mengenkripsi jumlah dengan base64
df = df.withColumn("jumlah_encrypted",
                   base64(col("jumlah").cast("string")))

# Menulis hasil streaming ke format parquet
query = df.writeStream \
    .format("parquet") \
    .option("path", "stream_data/realtime_output/") \
    .option("checkpointLocation", "data/checkpoints/") \
    .start()

query.awaitTermination()