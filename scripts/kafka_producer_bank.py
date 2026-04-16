from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Memulai pengiriman data transaksi bank (Mode Realistis)...")

while True:
    # 1. Skenario Jumlah Transaksi: 85% normal (kecil), 15% mencurigakan (besar)
    if random.random() < 0.85:
        jumlah_transaksi = random.randint(100000, 25000000) # Normal: 100rb - 25 Juta
    else:
        jumlah_transaksi = random.randint(55000000, 100000000) # Fraud: di atas 50 Juta

    # 2. Skenario Lokasi: 90% di Jakarta, 10% di Luar Negeri
    lokasi_transaksi = random.choices(["Jakarta", "Luar Negeri"], weights=[90, 10])[0]

    data = {
        "nama": random.choice(["Andi", "Budi", "Citra", "Dewi", "Eko"]), # Saya tambah nama agar lebih variatif
        "rekening": str(random.randint(100000, 999999)),
        "jumlah": jumlah_transaksi,
        "lokasi": lokasi_transaksi
    }

    producer.send("bank_topic", value=data)
    print(f"Terkirim: {data}")
    time.sleep(2)