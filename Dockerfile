FROM python:3.10-slim

WORKDIR /app

# Install dependencies build
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy project
COPY . .

# Upgrade pip, setuptools, wheel
RUN pip install --upgrade pip setuptools wheel

# Install package dari pyproject.toml
RUN pip install .

# Clone dataset (jika diperlukan)
# RUN git clone https://github.com/fadilf24/Machine_Learning_YOLO.git /app/data

# Entry point CLI
CMD ["bsort"]
