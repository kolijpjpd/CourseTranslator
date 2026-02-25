# SRT Suite - Windows Edition v1.0 Beta By RedBit 🚀

**SRT Suite** is a high-performance, AI-powered toolkit designed for cybersecurity professionals, educators, and content creators. It provides an all-in-one solution for generating high-accuracy subtitles (SRT/VTT) from video files and translating them using state-of-the-art LLMs.

---

## ✨ Key Features

- **Ultra-Fast Transcription**: Powered by `faster-whisper` (CTranslate2), providing 4x-10x speedup compared to standard OpenAI Whisper.
- **Dual Speed Modes**: Choose between **Fast** (minimal resource usage) and **Accurate** (maximum precision).
- **Pro Translation Engine**: Seamless integration with Zhipu AI (GLM-4) for context-aware, professional translations.
- **RTL & Arabic Optimization**: Automatic Unicode fixing for RTL languages to ensure perfect subtitle alignment in players like VLC and MPC.
- **Batch Processing**: Convert or translate multiple files simultaneously with thread-safe operations.
- **Privacy First**: Local AI models for transcription; your videos never leave your machine.

---

## 🛠 Prerequisites

To ensure peak performance on Windows, we recommend:
- **Python 3.10+** (if building from source).
- **FFmpeg**: Essential for audio extraction (Auto-installer included in the app).
- **Visual C++ Redistributable**: Required for the [ctranslate2](file:///home/kali/.local/lib/python3.13/site-packages/faster_whisper/transcribe.py#1873-1877) backend.

---

## 🚀 Getting Started (Build from Source)

If you have downloaded the **SRTSuite_Windows_Build_Package.zip**, follow these steps to create your professional, protected executable:

### 1. Environment Setup
- **Install Python**: Download and install [Python 3.10+](https://www.python.org/downloads/windows/).
  > [!IMPORTANT]
  > During installation, check the box **"Add Python to PATH"** and ensure **"tcl/tk and IDLE"** is selected under Optional Features.

### 2. Install Dependencies
Open your Terminal (CMD or PowerShell) and run the following command:
```batch
pip install pyinstaller faster-whisper ctranslate2 cryptography onnxruntime tkinterdnd2
```

### 3. Build the Executable
- Extract the ZIP package to a folder on your Desktop.
- Double-click the [build_windows.bat](file:///home/kali/%D8%AA%D8%B1%D8%AC%D9%85%D8%A9/backup/build_windows.bat) file.
- A terminal will open and begin the build process. This may take a few minutes as it compiles all AI models and GUI resources.
- Once finished, you will find your standalone app in the **`dist`** folder as `SRTSuite.exe`.

### 4. Setup & Launch
- Launch `dist\SRTSuite.exe`.
- Click the **"Install Requirements"** button (Green button top right) to finalize the `ffmpeg` configuration.

---

## 🔐 License Activation
The app requires activation on first launch. Use the provided **6-Month Universal License**:

1.  Open [universal_license.json](file:///home/kali/%D8%AA%D8%B1%D8%AC%D9%85%D8%A9/backup/universal_license.json) and copy its content.
2.  Paste it into the activation window in the app.
3.  Click **"ACTIVATE LICENSE"**.

*Valid for all devices until August 25, 2026.*

---

## 🤝 Contact & Support
Join our community for updates and support:
- **Telegram**: [@LIMEDARKK](https://t.me/+5JrSHhoH1jw3MjIx)
- **Developer**: Designed by **RED BIT**

---
© 2026 SRT Suite | Advanced Evasion & Automation Tactics.
