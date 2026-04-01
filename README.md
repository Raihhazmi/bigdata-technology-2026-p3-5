# 🚀 Modul Praktikum 3  - 4
## Batch Data Analytics & Visualization Layer with Spark and Power BI

![Dashboard Screenshot](reports/dashboard.png)
*(Ganti placeholder ini dengan screenshot hasil akhir Power BI kamu)*

Repositori ini berisi kelanjutan implementasi *pipeline* data berbasis **Apache Spark (PySpark)**, yang kini diintegrasikan dengan **Microsoft Power BI** untuk membangun layer visualisasi dan *Business Intelligence* (BI).

Proyek ini merupakan bagian dari Praktikum **Big Data Technology** Program Studi Teknologi Informasi – UIN Antasari.

---

## 📌 Deskripsi Proyek

Proyek ini mensimulasikan tahap akhir dari arsitektur Big Data modern: **Analytics & Visualization Layer**. 

Melanjutkan dari arsitektur Medallion di Modul 2, data yang sudah bersih (*Curated*) diproses lebih lanjut menjadi *insight* bisnis:
1. **Analytics Layer (PySpark):** Melakukan agregasi metrik bisnis (Total Revenue, Top Products, Revenue per Category) dan menyimpannya ke dalam *Serving Layer*.
2. **Visualization Layer (Power BI):** Mengimpor data dari *Serving Layer* untuk membangun *dashboard* analitik interaktif yang siap digunakan oleh level manajerial dan eksekutif perusahaan untuk pengambilan keputusan.

---

## 🛠️ Environment & Teknologi

- **Bahasa Pemrograman**: Python 3
- **Engine Pemrosesan Data**: Apache Spark (PySpark)
- **Business Intelligence Platform**: Microsoft Power BI Desktop
- **Visualisasi Python**: Matplotlib, Pandas
- **Sistem Operasi**: Linux Environment (WSL - Ubuntu) & Windows
- **Code Editor**: Visual Studio Code + Remote WSL Extension
- **Format Penyimpanan**: Parquet (Data Lake) & CSV (Serving/BI Layer)

---

## 📂 Struktur Direktori

Struktur proyek kini memiliki tambahan layer untuk *Serving* dan laporan visual:

```text
bigdata-project/
├── data/
│   ├── raw/        # Data mentah (CSV)
│   ├── clean/      # Data tervalidasi (Parquet)
│   ├── curated/    # Data siap analitik (Parquet)
│   └── serving/    # Data agregasi siap konsumsi BI (CSV)
├── reports/        # Hasil export visualisasi (.png) & file Dashboard (.pbix)
├── logs/           # Log eksekusi pipeline
├── scripts/
│   ├── batch_pipeline_enterprise.py
│   └── analytics_visualization.py
└── README.md
```
# ⚙️ Setup & Instalasi

## 1️⃣ Persiapan PySpark & Dependensi Python
(Pastikan setup **WSL** dan **Java 17** dari Modul 2 sudah berjalan)

Aktifkan virtual environment dan tambahkan library visualisasi:

```bash
source venv/bin/activate
pip install pyspark pandas matplotlib
```
----
# 2️⃣ Persiapan Power BI

Unduh dan instal Microsoft Power BI Desktop di sistem Windows Anda melalui tautan resmi Microsoft atau Microsoft Store.
-----

🚀 Cara Menjalankan Pipeline & Visualisasi
Langkah 1: Generate Analytics Data (Serving Layer)

Buka terminal di VS Code (mode WSL)

- Aktifkan virtual environment:
```
source venv/bin/activate
```
- Jalankan skrip agregasi Spark untuk membuat data metrik:
```
python scripts/analytics_visualization.py
```
Output yang dihasilkan:
 - File CSV metrik di folder data/serving/
 - Gambar grafik dasar di folder reports/

 ----
# Langkah 2: Build Power BI Dashboard

1. Buka Power BI Desktop
2. Pilih Get Data → Text/CSV
3. Muat file CSV dari folder data/serving/
4. Buat visualisasi berikut:

KPI Card
- Total Revenue → total_revenue.csv
Clustered Bar Chart
- Top 5 Products → top_products.csv
- Sort Descending
Clustered Bar Chart
- Revenue per Category → category_revenue.csv

Layout Dashboard

Tambahkan Text Box dengan:
- Judul:
```
E-Commerce Sales Dashboard
```
Subtitle:
```
Batch Analytics – Big Data Technology
```
Simpan file sebagai:
```
reports/dashboard_ecommerce.pbix
```
# 🧠 Konsep yang Diimplementasikan
✅ Serving Layer Pattern
Mengubah data Data Lake (Parquet) yang masif menjadi tabel agregasi kecil (CSV) yang sangat cepat di-load oleh tools BI.
Hal ini mengurangi beban query pada sistem dan mempercepat proses rendering visualisasi.
✅ Key Performance Indicator (KPI) Design
Menentukan dan menghitung metrik utama yang relevan untuk bisnis, seperti Total Revenue, agar performa e-commerce dapat dipahami secara cepat oleh stakeholder.
✅ Data Visualization Principles
MEmilih jenis grafik yang tepat:
- Bar Chart → untuk perbandingan kategori atau produk
- Sorting data → agar insight langsung terlihat tanpa analisis manual.
----

---

## 📊 Output Pipeline

Arsitektur data yang dihasilkan dari awal hingga akhir:

| Layer / Tahap   | Teknologi | Format  | Kegunaan                              |
|-----------------|-----------|---------|----------------------------------------|
| Raw             | CSV       | CSV     | Data mentah sumber                     |
| Clean / Curated | PySpark   | Parquet | Data tervalidasi & siap analitik       |
| Serving         | PySpark   | CSV     | Data agregasi ringan untuk BI          |
| Visualization   | Power BI  | .pbix   | Dashboard interaktif                   |

----
📈 Use Case & Pengembangan Lanjutan

Pipeline ini dapat dikembangkan lebih lanjut untuk:
- Integrasi otomatisasi penjadwalan dengan Apache Airflow
- Deployment ke ekosistem Cloud
  - AWS S3
  - GCP Cloud Storage
- Pembuatan filter interaktif (Slicer) berdasarkan rentang tanggal di Power BI
----
👨‍💻 Author

- Muhammad Raihan Azmi
- Praktikum Big Data Technology – 2026
Program Studi Teknologi Informasi
UIN Antasari

```
Jika Anda mau, saya juga bisa bantu membuat **versi README.md yang lebih profesional seperti repository GitHub (lengkap dengan badge, arsitektur pipeline diagram, dan struktur folder project)** supaya terlihat seperti **project Big Data production-ready**.
```
