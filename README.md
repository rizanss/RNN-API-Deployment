# ✍️ The AI Poet API (LSTM + FastAPI + Docker)

![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green.svg)
![Docker](https://img.shields.io/badge/Docker-Powered-blue.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

## 📄 Project Overview

Proyek ini adalah implementasi **end-to-end MLOps** untuk sebuah model *Natural Language Generation* (NLG). Model **Stacked Long Short-Term Memory (LSTM)** yang telah dilatih pada karya-karya Shakespeare di-deploy sebagai sebuah **API service interaktif menggunakan FastAPI dan sepenuhnya terbungkus dalam kontainer Docker.**

Aplikasi ini memungkinkan user untuk memberikan sebuah "umpan" kalimat dan akan menghasilkan teks baru yang meniru gaya bahasa Shakespeare, dengan tingkat kreativitas yang dapat diatur.

---

## ✨ Features

* **API Endpoint `/generate`**: Menerima input `seed_text` dan parameter `temperature` untuk menghasilkan teks baru.
* **Kontrol Kreativitas**: Parameter `temperature` memungkinkan pengguna untuk menyeimbangkan antara koherensi (temp rendah) dan kreativitas (temp tinggi) dari teks yang dihasilkan.
* **Dockerized & Portable**: Seluruh aplikasi dibungkus dalam sebuah Docker image, memastikan konsistensi dan kemudahan *deployment* di environment manapun.
* **Dokumentasi API Otomatis**: Dilengkapi dengan Swagger UI di endpoint `/docs` untuk kemudahan testing dan interaksi.

---

## 🛠️ Tech Stack

* **Model**: TensorFlow (Keras)
* **API Framework**: FastAPI
* **Web Server**: Uvicorn
* **Containerization**: Docker
* **Dependencies**: Python 3.11, NumPy

---

## 📂 Project Structure

```
Project-RNN-API-Deployment/
├── models/
│   └── shakespeare_lstm.weights.h5  # Model LSTM terbaik
│
├── notebooks/
│   └── LSTM_Text_Generator.ipynb            # Notebook untuk eksperimen
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── main.py                                  # Logika utama aplikasi FastAPI
├── README.md
├── shakespeare.txt
└── requirements.txt
```

---

## 🚀 How to Run with Docker

Pastikan Anda sudah meng-install **Docker Desktop** dan menjalankannya.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rizanss/RNN-API-Deployment.git](https://github.com/rizanss/RNN-API-Deployment.git)
    cd RNN-API-Deployment
    ```

2.  **Build the Docker image:**
    Perintah ini akan merakit aplikasi ke dalam sebuah *image* bernama `rnn-api`.
    ```bash
    docker build -t rnn-api:1.0 .
    ```

3.  **Run the Docker container:**
    Perintah ini akan menyalakan kontainer dan menghubungkan port `8000` di laptop Anda ke port `80` di dalam kontainer.
    ```bash
    docker run -p 8000:80 rnn-api:1.0
    ```

4.  **Aplikasi Anda sekarang berjalan!** Buka browser dan akses dokumentasi interaktif di [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

---

## 🧪 API Usage Example

Anda bisa mengetes API melalui halaman `/docs` atau menggunakan `curl`.

**Contoh menggunakan `curl`:**
```bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/generate](http://127.0.0.1:8000/generate)' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "seed_text": "To be, or not to be:",
  "chars_to_gen": 300,
  "temperature": 0.5
}'
```

**Contoh Response Sukses:**
```json
{
  "seed_text": "To be, or not to be:",
  "generated_text": " that the sould be the heart of his father's son,\nAnd the people of the state of the sould the sense\nTo the people of the state of the sould the souldier\nAnd so the sould be the state of the state.\n\nKING RICHARD II:\nWhat shall I say to my soul of the people?",
  "temperature": 0.5
}
```

---

## 📬 Contact
* **Author:** Riza Nursyah
* **GitHub:** [rizanss](https://github.com/rizanss)
* **LinkedIn:** [Riza Nursyah](https://www.linkedin.com/in/riza-nursyah-31a6a7221/)