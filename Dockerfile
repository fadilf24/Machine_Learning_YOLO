FROM python:3.10-slim

WORKDIR /app

# Install build tools & git
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

# Clone dataset dari GitHub (ganti URL sesuai repo dataset Anda)
RUN git clone https://github.com/username/dataset-bottlecaps.git data

# Entry point
CMD ["bsort"]
