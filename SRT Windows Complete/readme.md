# 🎬 SRT Suite — MP4 to SRT & Professional Translator (Windows Release)


**SRT Suite** is a high-performance tool designed for video transcription and automated subtitle translation. This build is **specifically optimized and obfuscated for Windows**.

## 🚀 Features
- **High-Speed Transcription:** Powered by `faster-whisper`.
- **Direct Windows Integration:** Native `.pyd` runtime for maximum performance.
- **Smart Translation:** Arabic-first professional translation using GLM-4 AI.
- **Stable Timing:** Optimized for Windows threading models.

## 🛠️ Installation

### 1. Requirements
- Python 3.10 or newer installation.
- FFmpeg installed in your System PATH (Crucial for transcription).

### 2. Setup
Open PowerShell or CMD in this folder:
```cmd
pip install -r requirements.txt
```

## 🎮 Execution
```cmd
python main.py
```

## ⚠️ Important for Windows Users
The core logic is protected by a native Windows library (`pyarmor_runtime.pyd`). Do not delete or move this file from its dedicated folder.

---
Developed by **@LIMEDARKK**
