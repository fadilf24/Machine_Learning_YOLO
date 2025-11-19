FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy semua file project
COPY . .

# Upgrade pip dan install build tools
RUN pip install --upgrade pip setuptools wheel

# Install package dari pyproject.toml
RUN pip install .

# Entry point
CMD ["bsort"]
