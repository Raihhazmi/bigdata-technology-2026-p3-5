# 🚀 Modul Praktikum 5: Real-Time Smart Transportation Analytics
## Decision-Oriented System with Apache Spark Streaming & Streamlit

![Dashboard Screenshot](reports/dashboard_transportation.png)
*(Ganti placeholder ini dengan screenshot hasil akhir Streamlit Dashboard kamu)*

[cite_start]Repositori ini berisi implementasi *pipeline* data berbasis **Apache Spark Structured Streaming** dan **Streamlit** untuk membangun sistem analitik *real-time* di domain Smart Transportation[cite: 8, 39, 46]. [cite_start]Sistem ini tidak hanya memvisualisasikan data, tetapi juga bertindak sebagai **Decision-Oriented System** yang memberikan *insight* dan *alert* otomatis untuk mendukung pengambilan keputusan yang cepat[cite: 24, 25, 26, 57].

[cite_start]Proyek ini merupakan bagian dari Praktikum **Big Data Technology** Program Studi Teknologi Informasi – UIN Antasari[cite: 3].

---

## 📌 Deskripsi Proyek

[cite_start]Proyek ini mensimulasikan arsitektur Big Data modern untuk pemrosesan data *streaming* (*Lambda/Kappa Architecture*)[cite: 708, 709]. Pipeline memproses data mobilitas kendaraan secara langsung (*real-time*) dan menghasilkan:
1. [cite_start]**Streaming Layer (PySpark):** Membaca aliran data JSON secara *real-time* dan menyimpannya secara efisien ke dalam format kolumnar *Parquet* di *Serving Layer*[cite: 36, 39, 50, 51].
2. [cite_start]**Analytics & Alerting Layer (Pandas):** Menghitung metrik utama (KPI), mendeteksi jam sibuk (*Peak Hour*), mendeteksi anomali perjalanan, dan men-*generate* peringatan lalu lintas (*Traffic Alerts*)[cite: 53, 54, 59, 60, 210, 305].
3. [cite_start]**Visualization Layer (Streamlit):** Membangun *dashboard* interaktif yang melakukan *auto-refresh* setiap 5 detik untuk menampilkan *Live Trip Data*, tren mobilitas, dan peringatan operasional[cite: 46, 259, 260].

---

## 🛠️ Environment & Teknologi

- [cite_start]**Bahasa Pemrograman**: Python 3 [cite: 9]
- [cite_start]**Engine Pemrosesan Data**: Apache Spark (PySpark Structured Streaming) [cite: 9, 39]
- [cite_start]**Real-Time Visualization**: Streamlit [cite: 9]
- [cite_start]**Data Analytics & Manipulasi**: Pandas [cite: 139]
- [cite_start]**Sistem Operasi**: Linux Server Environment (WSL - Ubuntu) [cite: 9]
- [cite_start]**Code Editor**: Visual Studio Code (Remote WSL) [cite: 9]
- [cite_start]**Format Penyimpanan**: JSON (Ingestion) & Parquet (Data Lake/Serving) [cite: 36, 40]

---

## 📂 Struktur Direktori

[cite_start]Sistem ini menggunakan arsitektur modular yang memisahkan logika berdasarkan domain (*Multi-Domain Pipeline*)[cite: 62, 63]:

```text
bigdata-project/
├── alerts/
│   ├── __init__.py                     # Wajib agar dikenali sebagai modul [cite: 87]
│   └── transportation_alert.py         # Logika deteksi alert lalu lintas [cite: 80, 217]
├── analytics/
│   ├── __init__.py                     # Wajib agar dikenali sebagai modul [cite: 87]
│   └── transportation_analytics.py     # Logika pemrosesan analitik dan metrik [cite: 76, 138]
├── dashboard/
│   └── dashboard_transportation.py     # UI Streamlit untuk real-time dashboard [cite: 82, 229]
├── data/
│   ├── checkpoints/transportation/     # Menyimpan state Spark Streaming [cite: 86]
│   └── serving/transportation/         # Data Parquet hasil pemrosesan [cite: 84, 85]
├── scripts/
│   └── transportation/
│       ├── streaming_trip_layer.py     # Script PySpark untuk ingest & sink data [cite: 117]
│       └── trip_generator.py           # Script pembuat data dummy (JSON) [cite: 90]
├── stream_data/
│   └── transportation/                 # Folder tempat data JSON masuk [cite: 93]
└── README.md
```
-----
#### ⚙️ Setup & Instalasi
Pastikan Anda menjalankan proyek ini dari Root Project Directory (bigdata-project/)
1. Aktifkan virtual environment:
   ```Bash
   source venv/bin/activate
   ```
2. Instal pustaka yang dibutuhkan:
   ```Bash
   pip install pyspark pandas streamlit
   ```

#### 🚀 Cara Menjalankan Pipeline (Wajib Berurutan)
Untuk menjalankan ekosistem real-time ini, Anda harus membuka 3 Terminal secara bersamaan dan menjalankannya dengan urutan berikut:

- Terminal 1: Jalankan Spark Streaming Engine
Berfungsi membaca data dari stream_data/transportation dan menulisnya dalam format Parquet ke data/serving/transportation.
```Bash
spark-submit scripts/transportation/streaming_trip_layer.py
```

Gemini berkata
Wah, selamat ya sudah berhasil menyelesaikan praktikumnya, Azmi! 🎉 Menyelesaikan pipeline streaming data real-time dengan Spark dan Streamlit itu pencapaian yang keren banget.

Karena kamu sudah masuk ke tahap Modul 5: Smart Transportation & Decision-Oriented System, isi README.md kamu harus dirombak total dari yang sebelumnya berbasis Batch Processing (Modul 3-4) menjadi Real-Time Streaming.

Berikut adalah draf pembaruan README.md yang sudah saya susun dengan gaya profesional ala repository GitHub production-ready, lengkap dengan arsitektur dan instruksi eksekusi sesuai Modul 5:

Markdown
# 🚀 Modul Praktikum 5: Real-Time Smart Transportation Analytics
## Decision-Oriented System with Apache Spark Streaming & Streamlit

![Dashboard Screenshot](reports/dashboard_transportation.png)
*(Ganti placeholder ini dengan screenshot hasil akhir Streamlit Dashboard kamu)*

[cite_start]Repositori ini berisi implementasi *pipeline* data berbasis **Apache Spark Structured Streaming** dan **Streamlit** untuk membangun sistem analitik *real-time* di domain Smart Transportation[cite: 8, 39, 46]. [cite_start]Sistem ini tidak hanya memvisualisasikan data, tetapi juga bertindak sebagai **Decision-Oriented System** yang memberikan *insight* dan *alert* otomatis untuk mendukung pengambilan keputusan yang cepat[cite: 24, 25, 26, 57].

[cite_start]Proyek ini merupakan bagian dari Praktikum **Big Data Technology** Program Studi Teknologi Informasi – UIN Antasari[cite: 3].

---

## 📌 Deskripsi Proyek

[cite_start]Proyek ini mensimulasikan arsitektur Big Data modern untuk pemrosesan data *streaming* (*Lambda/Kappa Architecture*)[cite: 708, 709]. Pipeline memproses data mobilitas kendaraan secara langsung (*real-time*) dan menghasilkan:
1. [cite_start]**Streaming Layer (PySpark):** Membaca aliran data JSON secara *real-time* dan menyimpannya secara efisien ke dalam format kolumnar *Parquet* di *Serving Layer*[cite: 36, 39, 50, 51].
2. [cite_start]**Analytics & Alerting Layer (Pandas):** Menghitung metrik utama (KPI), mendeteksi jam sibuk (*Peak Hour*), mendeteksi anomali perjalanan, dan men-*generate* peringatan lalu lintas (*Traffic Alerts*)[cite: 53, 54, 59, 60, 210, 305].
3. [cite_start]**Visualization Layer (Streamlit):** Membangun *dashboard* interaktif yang melakukan *auto-refresh* setiap 5 detik untuk menampilkan *Live Trip Data*, tren mobilitas, dan peringatan operasional[cite: 46, 259, 260].

---

## 🛠️ Environment & Teknologi

- [cite_start]**Bahasa Pemrograman**: Python 3 [cite: 9]
- [cite_start]**Engine Pemrosesan Data**: Apache Spark (PySpark Structured Streaming) [cite: 9, 39]
- [cite_start]**Real-Time Visualization**: Streamlit [cite: 9]
- [cite_start]**Data Analytics & Manipulasi**: Pandas [cite: 139]
- [cite_start]**Sistem Operasi**: Linux Server Environment (WSL - Ubuntu) [cite: 9]
- [cite_start]**Code Editor**: Visual Studio Code (Remote WSL) [cite: 9]
- [cite_start]**Format Penyimpanan**: JSON (Ingestion) & Parquet (Data Lake/Serving) [cite: 36, 40]

---

## 📂 Struktur Direktori

[cite_start]Sistem ini menggunakan arsitektur modular yang memisahkan logika berdasarkan domain (*Multi-Domain Pipeline*)[cite: 62, 63]:

```text
bigdata-project/
├── alerts/
│   ├── __init__.py                     # Wajib agar dikenali sebagai modul [cite: 87]
│   └── transportation_alert.py         # Logika deteksi alert lalu lintas [cite: 80, 217]
├── analytics/
│   ├── __init__.py                     # Wajib agar dikenali sebagai modul [cite: 87]
│   └── transportation_analytics.py     # Logika pemrosesan analitik dan metrik [cite: 76, 138]
├── dashboard/
│   └── dashboard_transportation.py     # UI Streamlit untuk real-time dashboard [cite: 82, 229]
├── data/
│   ├── checkpoints/transportation/     # Menyimpan state Spark Streaming [cite: 86]
│   └── serving/transportation/         # Data Parquet hasil pemrosesan [cite: 84, 85]
├── scripts/
│   └── transportation/
│       ├── streaming_trip_layer.py     # Script PySpark untuk ingest & sink data [cite: 117]
│       └── trip_generator.py           # Script pembuat data dummy (JSON) [cite: 90]
├── stream_data/
│   └── transportation/                 # Folder tempat data JSON masuk [cite: 93]
└── README.md
```
### ⚙️ Setup & Instalasi
Pastikan Anda menjalankan proyek ini dari Root Project Directory (bigdata-project/).

Aktifkan virtual environment:

```Bash
source venv/bin/activate
```

Instal pustaka yang dibutuhkan:
```Bash
pip install pyspark pandas streamlit
```

### 🚀 Cara Menjalankan Pipeline (Wajib Berurutan)
Untuk menjalankan ekosistem real-time ini, Anda harus membuka 3 Terminal secara bersamaan dan menjalankannya dengan urutan berikut:

Terminal 1: Jalankan Spark Streaming Engine
Berfungsi membaca data dari stream_data/transportation dan menulisnya dalam format Parquet ke data/serving/transportation.

``` Bash
spark-submit scripts/transportation/streaming_trip_layer.py
```

Terminal 2: Jalankan Data Generator
Mensimulasikan sensor kendaraan yang mengirimkan data trip setiap 3 detik.

```Bash
python scripts/transportation/trip_generator.py
```
Terminal 3: Jalankan Streamlit Dashboard
Membaca data secara berkala dan menampilkan visualisasi serta sistem peringatan dini.

```Bash
streamlit run dashboard/dashboard_transportation.py
```
👉 Akses dashboard di browser: http://localhost:8501

---- 

### 🧠 Insight & Arsitektur KeputusanSistem ini mendukung 3 lapis pengambilan keputusan (Decision-Oriented System):
1. Real-Time Decision (Operasional): - Traffic Alerts (contoh: "High traffic volume") dan Live Trip Data untuk penyesuaian rute atau pelacakan pelanggan seketika.
2. Tactical Decision (Near Real-Time): - Visualisasi Vehicle Distribution dan Fare per Location untuk menyeimbangkan penempatan armada (fleet balancing) dan mengoptimalkan harga (dynamic pricing).
3. Strategic Decision (Historikal): - Mobility Trend dan Abnormal Trips untuk mendeteksi potensi kecurangan (fraud detection) dan melakukan peramalan permintaan (demand forecasting).

-----
### 👨‍💻 Author
Muhammad Raihan Azmi 
Praktikum Big Data Technology – 2026 
Program Studi Teknologi Informasi 
UIN Antasari 
