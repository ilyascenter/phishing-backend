#  Phishing URL Detection - Backend

Backend API untuk mendeteksi URL phishing menggunakan Machine Learning berbasis Python (Flask + Scikit-learn).

---

##  Fitur Utama

*  Deteksi URL: **Phishing / Suspicious / Legit**
*  Machine Learning (Random Forest)
*  Confidence score (%)
*  Explainable AI (alasan deteksi)
*  Rate limiting (anti spam)
*  REST API (Flask + CORS)
*  Production-ready (Waitress)

---

##  Cara Kerja Sistem

1. User mengirim URL ke endpoint `/predict`
2. Backend melakukan:

   * Feature extraction dari URL
   * Prediksi menggunakan model Machine Learning
3. API mengembalikan:

   * prediction (Phishing / Suspicious / Legit)
   * confidence (%)
   * reasons (alasan deteksi)

---

##  Struktur Project

phishing-backend/
├── app.py
├── feature.py
├── train.py
├── model.pkl
├── requirements.txt
└── README.md

---

##  Instalasi

### 1. Clone Repository

git clone https://github.com/username/phishing-backend.git
cd phishing-backend

---

### 2. Install Dependency

pip install -r requirements.txt

---

### 3. Training Model

python train.py

File `model.pkl` akan otomatis dibuat.

---

### 4. Jalankan Server

python app.py

Server akan berjalan di:

http://localhost:5000

---

##  API Endpoint

###  GET /

Cek status API

Response:
{
"status": "API jalan"
}

---

###  POST /predict

Request:
{
"url": "http://example.com"
}

Response:
{
"url": "http://example.com",
"prediction": "Phishing",
"confidence": 85.5,
"reasons": [
"Mengandung kata 'login'",
"Mengandung dash (-)"
]
}

---

##  Feature Extraction

Model menggunakan beberapa fitur dari URL, seperti:

* Panjang URL
* Jumlah titik (.)
* HTTPS atau tidak
* Panjang domain
* Domain mengandung angka
* IP address dalam URL
* TLD mencurigakan (.tk, .ml, dll)
* Keyword phishing (login, verify, secure, dll)
* Karakter khusus (@, %)
* URL terlalu panjang

---

##  Security

* Rate limit per IP (2 detik)
* CORS enabled
* Disarankan menambahkan API key untuk produksi

---

##  Deployment

Backend dapat dijalankan di:

* VPS (Windows / Linux)
* Local server

Menggunakan:

Waitress sebagai production server

---

##  Catatan

* Model masih menggunakan dataset sederhana
* Untuk hasil lebih akurat, gunakan dataset real (Kaggle / Open Dataset)

---


