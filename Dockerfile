# Use the official Python 3.12 slim image
FROM python:3.12-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# --- UPDATED STEP: Install system dependencies ---
RUN apt-get update && apt-get install -y \
    # Provides C compilers (gcc) needed for building extensions
    build-essential \
    # Provides the pkg-config tool, required by mysqlclient
    pkg-config \
    # Provides development headers for MySQL, required by mysqlclient
    default-libmysqlclient-dev \
    # Provides development headers for image support (JPEG, PNG), required by Pillow
    libjpeg-dev \
    zlib1g-dev \
    # Clean up apt cache to reduce final image size
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the project files into the container
COPY . .