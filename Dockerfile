FROM python:3.10-slim

WORKDIR /app

COPY . .

# Install system dependencies untuk build
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip dan install build tools PEP 517
RUN pip install --upgrade pip setuptools wheel

# Install package dari pyproject.toml (PEP 517)
RUN pip install --use-pep517 .

CMD ["bsort"]
