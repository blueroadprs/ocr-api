FROM python:3.10-slim

# Instala tesseract-ocr y sus dependencias
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-spa \
    libgl1 \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Crea directorio de la app
WORKDIR /app

# Copia el código
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Expone el puerto que usará Render
EXPOSE 5000

CMD ["python", "app.py"]
