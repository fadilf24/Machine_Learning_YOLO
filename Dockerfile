# Gunakan Python 3.10
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy pyproject.toml & requirements.txt
COPY pyproject.toml requirements.txt ./

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy semua kode Python dan folder configs, notebooks, tests
COPY bsort/ ./bsort/
COPY configs/ ./configs/
COPY notebooks/ ./notebooks/
COPY tests/ ./tests/

# Set entrypoint
ENTRYPOINT ["bsort"]
CMD ["--help"]
