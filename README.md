# 🛡️ Mini-SIEM (Mini Security Information & Event Management)

Mini-SIEM adalah **aplikasi sederhana untuk memantau log keamanan**, mendeteksi aktivitas mencurigakan, dan mengelola alert seperti yang dilakukan di **Security Operations Center (SOC)**.

Project ini dibuat sebagai **hands-on cybersecurity portfolio** untuk menunjukkan pemahaman tentang:
- log monitoring  
- detection rules  
- alerting  
- incident response  

Tanpa tools enterprise yang berat — semua dibangun dari nol dengan Python.

---

## ✨ Apa yang Bisa Dilakukan Project Ini?

### 🔹 Monitoring Log
- Membaca dan memproses file log (`auth.log`)
- Mengubah log mentah menjadi event yang rapi dan mudah dianalisis

### 🔹 Deteksi Keamanan
- Deteksi **SSH brute force**
- Deteksi **sudo authentication failure**
- Menggunakan rule sederhana seperti di SIEM sungguhan

### 🔹 Alert & Incident
- Membuat alert otomatis dari event mencurigakan
- Alert punya status **open / resolved**
- Bisa menambahkan catatan analis

### 🔹 Audit Log Search
- Cari log berdasarkan:
  - keyword
  - user
  - IP address
  - event type
- Konsep “Run Query” seperti tools SOC

### 🔹 Dashboard
- Ringkasan event & alert
- Tampilan SOC-style
- Mudah dipahami walaupun bukan security expert

---

## 🧠 Gambaran Cara Kerja

Log File
↓
Parser
↓
Detection Rules
↓
Events & Alerts
↓
Dashboard / Incident Response

Sederhana, tapi mencerminkan alur kerja SIEM di dunia nyata.

---

## 🛠️ Tech Stack

- Python
- Streamlit (UI & Dashboard)
- SQLite (database lokal)
- Regex-based parsing
- macOS friendly

---

## 📂 Struktur Project

mini-siem/
├── app.py # Main UI
├── main.py # Log ingestion
├── pages/ # Dashboard, Audit Logs, Incident Response
├── siem/ # Core SIEM logic
├── samples/ # Sample log file
├── data/ # Local database (ignored in Git)
└── README.md

