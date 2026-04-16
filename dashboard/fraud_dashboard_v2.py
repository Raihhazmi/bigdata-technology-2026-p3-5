import streamlit as st
import pandas as pd
import time

st.title("🚨 Real-Time Fraud Detection Dashboard")

try:
    # Mencoba membaca data parquet
    df = pd.read_parquet("stream_data/realtime_output/")
    
    # Jika berhasil, tampilkan metrik dan grafik
    st.metric("Total Transaksi", len(df))
    st.metric("Total Fraud", len(df[df["status"]=="FRAUD"]))

    st.dataframe(df.tail(10))
    st.bar_chart(df["status"].value_counts())

except Exception as e:
    # Jika file masih 0 byte atau belum ada, tampilkan pesan loading
    st.warning("⏳ Menunggu data masuk dari Spark... (Sedang memproses)")
    # Otomatis refresh halaman setiap 2 detik
    time.sleep(2)
    st.rerun()