# Gunakan base image Python 3.10 slim
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies build & git
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy semua file project ke container
COPY . .

# Upgrade pip, setuptools, wheel
RUN pip install --upgrade pip setuptools wheel

# Install package dari pyproject.toml
RUN pip install .

# Clone dataset dari GitHub
# Ganti URL dengan repo dataset Anda
RUN git clone https://github.com/fadilf24/Machine_Learning_YOLO.git data

# Pastikan struktur data benar
RUN ls -R data

# Set entrypoint CLI
CMD ["bsort"]
