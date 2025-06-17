# ===================================================================================
#  main.py - Otak Utama dari API Pujangga AI (RNN/LSTM)
# ===================================================================================

# --- 1. Import Library yang Dibutuhkan ---
import os
import uvicorn
import numpy as np
import tensorflow as tf
from fastapi import FastAPI
from pydantic import BaseModel
import sys

# --- 2. Inisialisasi Aplikasi FastAPI ---
app = FastAPI(title="AI Poet - Shakespeare Text Generator",
              description="API untuk menghasilkan teks baru dengan gaya penulisan Shakespeare menggunakan model LSTM.",
              version="1.0")

# --- 3. Load Aset-Aset Penting ---
# Ini adalah bagian yang paling berbeda dari proyek CNN kita.
# Kita harus me-load model DAN membangun ulang "kamus" kita.

# --- Re-create "kamus" dari file teks asli ---
text = open('shakespeare.txt', 'rb').read().decode(encoding='utf-8')
chars = sorted(list(set(text)))
vocab_size = len(chars)
char_to_int = {char: i for i, char in enumerate(chars)}
int_to_char = {i: char for i, char in enumerate(chars)}
SEQ_LENGTH = 100

# --- FUNGSI UNTUK MEMBANGUN ULANG ARSITEKTUR MODEL ---
# Arsitektur ini harus SAMA PERSIS dengan yang di notebook training
def build_model(vocab_size, seq_length):
    model = tf.keras.models.Sequential([
        tf.keras.layers.LSTM(256, input_shape=(seq_length, 1), return_sequences=True),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.LSTM(256),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(vocab_size, activation='softmax')
    ])
    return model

# --- Load Aset-Aset Penting ---
try:
    # 1. Bangun ulang "badan" model yang kosong
    model = build_model(vocab_size, SEQ_LENGTH)

    # 2. "Masukkan otaknya" (load weights) ke badan yang sudah ada
    weights_path = os.path.join("models", "shakespeare_lstm.weights.h5")
    model.load_weights(weights_path)

    print("Model architecture built and weights loaded successfully!")

except Exception as e:
    model = None
    print(f"Error loading assets: {e}")


# ... SISA KODE (RequestBody dan endpoint /generate) TETAP SAMA PERSIS ...
# Pastikan tidak ada yang diubah dari sini ke bawah
class RequestBody(BaseModel):
    seed_text: str
    chars_to_gen: int = 300
    temperature: float = 0.5

@app.post("/generate", tags=["Text Generation"])
async def generate_text(body: RequestBody):
    """
    Endpoint untuk menghasilkan teks baru.

    - **seed_text**: Teks umpan untuk memulai proses generasi.
    - **chars_to_gen**: Jumlah karakter yang ingin dihasilkan.
    - **temperature**: Tingkat "kreativitas" (0.2 = konservatif, 1.2 = liar).
    """
    if model is None:
        return {"error": "Model tidak berhasil di-load. Cek log server."}

    # -- Preprocessing Input --
    pattern = [char_to_int.get(char, 0) for char in body.seed_text]

    generated_text = ""

    # -- Proses Generasi Teks --
    for i in range(body.chars_to_gen):
        input_pattern = tf.keras.preprocessing.sequence.pad_sequences([pattern], maxlen=SEQ_LENGTH, truncating='pre')

        x = np.reshape(input_pattern, (1, SEQ_LENGTH, 1))
        x = x / float(vocab_size)

        prediction = model.predict(x, verbose=0)
        # "Buka amplopnya": ambil elemen pertama dari hasil prediksi
        prediction = prediction[0]

        prediction = np.asarray(prediction).astype('float64')
        prediction = np.log(prediction) / body.temperature
        exp_preds = np.exp(prediction)
        prediction = exp_preds / np.sum(exp_preds)
        probas = np.random.multinomial(1, prediction, 1)
        index = np.argmax(probas)

        result = int_to_char[index]
        generated_text += result

        pattern.append(index)
        pattern = pattern[1:len(pattern)]

    return {
        "seed_text": body.seed_text,
        "generated_text": generated_text,
        "temperature": body.temperature
    }

@app.get("/", tags=["Health Check"])
def read_root():
    return {"status": "AI Poet API is running..."}