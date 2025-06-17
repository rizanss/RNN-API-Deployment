# ======================================================================
#  Dockerfile untuk API Pujangga AI (RNN)
# ======================================================================

# Tahap 1: Mulai dari base image RESMI TensorFlow.
# Ini sudah termasuk Python dan semua library TensorFlow.
FROM tensorflow/tensorflow:2.16.1

# Tahap 2: Siapkan "Area Kerja"
WORKDIR /app

# Tahap 3: Install "Perkakas Tambahan"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Tahap 4: Copy "Aset" dan "Otak" Aplikasi Kita
COPY . .

# Tahap 5: Perintah untuk "Menyalakan" Aplikasi
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]