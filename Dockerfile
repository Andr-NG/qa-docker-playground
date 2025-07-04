# Base image
FROM python:3.12-slim

# Work directory
WORKDIR /app

# Copy dependencies to WORKDIR and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Run with
CMD ["pytest", "tests"]