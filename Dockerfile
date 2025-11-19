# Gunakan base image Python 3.10 slim
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy semua file project ke container
COPY . .

# Upgrade pip, setuptools, wheel
RUN pip install --upgrade pip setuptools wheel

# Install package dari pyproject.toml
RUN pip install .

# Entry point CLI
CMD ["bsort"]
