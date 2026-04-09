# 🚀 Big Data Project: Smart Transportation & Traffic Prediction AI
## Integrasi Real-Time Analytics (Modul 5) & Machine Learning Pipeline (Modul 7)

![Dashboard Screenshot](reports/dashboard_transportation.png)
*(Ganti placeholder ini dengan screenshot hasil akhir Streamlit Dashboard kamu)*

[cite_start]Repositori ini berisi implementasi *pipeline* data komprehensif yang mencakup arsitektur Big Data modern untuk pemrosesan *streaming* (**Modul 5**) dan sistem prediksi cerdas berbasis Machine Learning (**Modul 7**)[cite: 5, 6]. [cite_start]Sistem ini dirancang sebagai **Decision-Oriented System** untuk domain Smart City AI[cite: 7].

Proyek ini merupakan bagian dari Praktikum **Big Data Technology** Program Studi Teknologi Informasi – UIN Antasari.

---

## 📌 Deskripsi Proyek

Sistem ini menggabungkan dua lapisan analitik utama:
1. **Real-Time Analytics Layer (Modul 5):** Menggunakan PySpark Structured Streaming untuk menyerap aliran data JSON secara *real-time*, menyimpannya ke format *Parquet*, dan men-*generate* peringatan dini (*Traffic Alerts*).
2. [cite_start]**Predictive Analytics Layer (Modul 7):** Menggunakan model Machine Learning **Random Forest** (Regresi) untuk melakukan prediksi volume kendaraan di masa depan[cite: 17, 18, 50]. [cite_start]Sistem ini melakukan *Feature Engineering* berbasis data runtun waktu (*Time-Series*) dengan memanfaatkan variabel `Jam`, `Hari`, dan `Lag`[cite: 27, 50].
3. [cite_start]**Visualization Layer:** *Dashboard* interaktif dengan **Streamlit Modern UI** untuk memantau data historis, *live streaming*, dan melakukan input parameter prediksi secara dinamis[cite: 19, 20, 28].

---

## 🏙️ Konteks Industri (Smart City AI)

[cite_start]Implementasi model prediksi *traffic* seperti pada proyek ini secara nyata digunakan dalam arsitektur Smart City global[cite: 30, 31]:
* [cite_start]**Adaptive Traffic Control System** & Prediksi kemacetan *real-time*[cite: 32, 33].
* [cite_start]**Smart Routing** (seperti sistem pada Google Maps dan Waze)[cite: 34].
* [cite_start]**Integrasi IoT sensor jalan** untuk memantau mobilitas[cite: 35].
* [cite_start]Diterapkan oleh perusahaan teknologi besar seperti Google (Traffic Prediction AI), IBM Smart City, dan Siemens Mobility[cite: 36, 37, 38, 39].

---

## 🛠️ Environment & Teknologi

* [cite_start]**Bahasa Pemrograman**: Python 3 [cite: 8, 9]
* [cite_start]**Big Data Engine**: Apache Spark (PySpark Structured Streaming) [cite: 16]
* [cite_start]**Machine Learning**: Scikit-Learn (Random Forest Regressor) [cite: 17, 18, 74]
* [cite_start]**Data Manipulasi & Cleaning**: Pandas [cite: 61]
* [cite_start]**Dashboarding**: Streamlit & Matplotlib [cite: 19, 20, 99, 102]
* [cite_start]**Environment**: Linux Server Environment (WSL - Ubuntu) via VS Code [cite: 10, 11, 12, 13, 14, 15]

---

## 📂 Struktur Direktori

Sistem menggunakan arsitektur modular yang memisahkan data mentah, proses *cleaning*, analitik, dan visualisasi (*Multi-Domain Pipeline*):

```text
bigdata-project/
├── analytics/
│   ├── transportation_analytics.py     # [Modul 5] Logika metrik streaming
│   └── traffic_ml_model_v1.py          # [Modul 7] Script training ML & Feature Engineering [cite: 72]
├── dashboard/
│   ├── dashboard_transportation.py     # [Modul 5] UI streaming real-time
│   └── traffic_dashboard_v1.py         # [Modul 7] UI Prediksi Traffic dengan Slider [cite: 98]
├── data/
│   ├── raw/
│   │   └── traffic_smartcity_v1.csv    # [Modul 7] Raw dataset traffic [cite: 52, 53, 56]
│   ├── clean/
│   │   └── traffic_smartcity_clean_v1.csv # [Modul 7] Data hasil cleaning [cite: 68]
│   ├── checkpoints/                    # [Modul 5] State Spark Streaming
│   └── serving/                        # [Modul 5] Data Parquet
├── models/
│   └── traffic_model_v1.pkl            # [Modul 7] Model ML yang telah dilatih [cite: 91, 94]
├── scripts/
│   ├── traffic_data_cleaning_v1.py     # [Modul 7] Proses pembersihan data [cite: 59, 60]
│   └── transportation/
│       ├── streaming_trip_layer.py     # [Modul 5] Spark streaming script
│       └── trip_generator.py           # [Modul 5] Generator data dummy JSON
└── README.md
```
### ⚙️ Setup & Instalasi
   - Pastikan terminal berada di Root Project Directory (bigdata-project/).
   - Aktifkan virtual environment:
      ```Bash
      source venv/bin/activate
      ```
   - Instal pustaka yang dibutuhkan:
      ```Bash
      pip install pyspark pandas scikit-learn streamlit matplotlib joblib
      ```
### 🚀 Cara Menjalankan Pipeline
   A. Menjalankan Machine Learning Pipeline (Modul 7)
   1. Lakukan eksekusi berurutan pada satu terminal untuk melatih model prediksi:
      ```Bash
      python scripts/traffic_data_cleaning_v1.py
      ```
      (Script ini akan menghasilkan file traffic_smartcity_clean_v1.csv )(Script ini akan menghasilkan file traffic_smartcity_clean_v1.csv )
   2. alankan Feature Engineering & ML Modeling:
      ```Bash
      python analytics/traffic_ml_model_v1.py
      ```
      (Script ini akan mengekstrak jam, hari, lag, melatih model Random Forest, dan menyimpannya sebagai traffic_model_v1.pkl )
      Jalankan pembersihan data (Data Cleaning):
   3.Jalankan Dashboard Prediksi:
      ```Bash
      streamlit run dashboard/traffic_dashboard_v1.py
      ```
      👉 Akses di browser: http://localhost:8501
### B. Menjalankan Streaming Pipeline (Modul 5)
Buka 3 terminal berbeda dan jalankan berurutan:
   * Terminal 1 (Spark Ingestion): spark-submit scripts/transportation/streaming_trip_layer.py
   * Terminal 2 (Data Generator): python scripts/transportation/trip_generator.py
   * Terminal 3 (Live Dashboard): streamlit run dashboard/dashboard_transportation.py

### 🧠 Insight & Arsitektur Keputusan
Integrasi Big Data dan AI menghasilkan wawasan strategis:
- Kekuatan ML: Machine Learning sangat powerful untuk memprediksi kemacetan. Bahkan dengan feature yang sederhana (Jam dan Hari), performa model sudah cukup kuat untuk memberikan taksiran yang akurat.
- Pentingnya Pipeline Data: Alur kerja (pembersihan -> pemodelan -> serving) adalah fondasi penting dalam membangun Big Data System di dunia nyata.
- Pengembangan Lanjutan: Di masa depan, sistem dapat berevolusi dengan mengintegrasikan antrean real-time via Apache Kafka/Spark dan transisi ke model Deep Learning seperti LSTM untuk forecast yang lebih canggih, mewujudkan ekosistem AI-driven decision system.

### 👨‍💻 Author
Muhammad Raihan Azmi Praktikum Big Data Technology – 2026
Program Studi Teknologi Informasi
UIN Antasari
