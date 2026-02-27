# 🎬 SRT Suite — MP4 to SRT & Professional Translator (Linux Release)

![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Linux-orange.svg)
![Security](https://img.shields.io/badge/Protection-Obfuscated-red.svg)

**SRT Suite** is a high-performance tool designed for video transcription and automated subtitle translation using state-of-the- art AI models. This build is **obfuscated** to protect intellectual property and ensure runtime integrity.

## 🛡️ Security & Integrity (MITRE ATT&CK Context)
This release employs advanced code obfuscation techniques to prevent unauthorized reverse engineering and tampering.
- **Technique:** [T1027 - Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027/)
- **Build Engine:** Pyarmor (Binary-level obfuscation)
- **Protection Scope:** Core logic, API integration, and License management systems are encrypted and executed in a dedicated runtime environment.

## 🚀 Features
- **High-Speed Transcription:** Powered by `faster-whisper`.
- **Word-Level Precision:** Syllable-accurate timing (Optimized in V6).
- **Smart Translation:** Arabic-first professional translation using GLM-4 AI.
- **RTL Support:** Correct Unicode handling for Arabic scripts (Bidi algorithm).
- **Stealth Runtime:** Minimal footprint with protected source nodes.

## 🛠️ Installation

### 1. Clone or Download
```bash
git clone <repository-url>
cd "SRT Linux Complete"
```

### 2. Install Dependencies
Ensure you have Python 3.10+ installed.
```bash
pip install -r requirements.txt
```

### 3. Permissions
Ensure the runtime library has execution permissions:
```bash
chmod +x pyarmor_runtime_000000/pyarmor_runtime.so
```

## 🎮 Execution
Run the main entry point:
```bash
python3 main.py
```

## ⚙️ Configuration
1. Go to **Settings** tab.
2. Enter your **Zhipu AI API Key** (GLM-4-Flash).
3. Save and start translating.

---
Developed by **@LIMEDARKK**
*For operational security and professional subtitle production.*
