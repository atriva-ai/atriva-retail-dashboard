# Use Ubuntu 24.04 as base
FROM ubuntu:24.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    wget \
    git \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    ffmpeg \
    python3.12 \
    python3.12-venv \
    python3.12-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set Python 3.12 as default
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1

# Create working directory
WORKDIR /app

# Copy project files
COPY . /app

# Create virtual environment
RUN python3 -m venv venv

# Activate venv and install Python dependencies
RUN . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose Panel's default port
EXPOSE 5006

# Start Panel app
CMD ["/bin/bash", "-c", "source venv/bin/activate && exec panel serve app.py --address 0.0.0.0 --allow-websocket-origin='*' --autoreload"]
# CMD ["/bin/bash"]
# activate venv and run --- panel serve app.py --address 0.0.0.0 --allow-websocket-origin=*
# Docker run using::: docker run -it --rm -v "$(pwd)":/app -w /app -p 5006:5006 retail-base bash
