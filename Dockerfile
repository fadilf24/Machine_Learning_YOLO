# Gunakan Python 3.10
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt ./

# Upgrade pip dan install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy semua kode
COPY bsort/ ./bsort/
COPY configs/ ./configs/
COPY notebooks/ ./notebooks/
COPY tests/ ./tests/
COPY README.md ./

# Set CLI entrypoint
ENTRYPOINT ["bsort"]
CMD ["--help"]
