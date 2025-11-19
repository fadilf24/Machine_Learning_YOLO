FROM python:3.10-slim

WORKDIR /app

# Install git untuk clone dataset
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy seluruh project
COPY . .

# Upgrade pip, setuptools, wheel
RUN pip install --upgrade pip setuptools wheel

# Install package dari pyproject.toml
RUN pip install .

# Clone dataset dari GitHub
# Ganti URL dataset kamu di sini
RUN git clone https://github.com/fadilf24/Machine_Learning_YOLO.git /app/data

# Pastikan struktur: /app/data/train dan /app/data/val
RUN ls /app/data

# Entry point CLI
CMD ["bsort"]
