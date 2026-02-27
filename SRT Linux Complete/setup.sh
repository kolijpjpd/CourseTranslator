#!/bin/bash

echo "🚀 Starting SRT Suite Setup..."

# Update and install system dependencies (ffmpeg is needed for faster-whisper)
if command -v apt-get &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y ffmpeg python3-pip
elif command -v dnf &> /dev/null; then
    sudo dnf install -y ffmpeg python3-pip
fi

# Install python requirements
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

# Set permissions
echo "🔐 Setting permissions..."
chmod +x pyarmor_runtime_000000/pyarmor_runtime.so

echo "✅ Setup Complete! Run the app using: python3 main.py"
