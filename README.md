# 🎬 SRT Suite: AI Video Transcription & Translation

![

**SRT Suite** is a state-of-the-art tool designed for high-precision video subtitle generation and automated translation. Leveraging the power of `faster-whisper` and Zhipu AI (GLM-4), it provides a seamless workflow from raw video to localized, perfectly-timed Arabic subtitles.

---

## 🌎 Releases (Choose Your Platform)

This repository is organized into platform-specific builds to ensure compatibility and maximum performance.

### 🐧 [SRT Linux Complete](./SRT%20Linux%20Complete/)
*   **Target:** Ubuntu, Kali, Debian, and other Linux distributions.
*   **Runtime:** Native `.so` obfuscation engine.
*   **Setup:** Includes `setup.sh` for automated FFmpeg and dependency installation.

### 🪟 [SRT Windows Complete](./SRT%20Windows%20Complete/)
*   **Target:** Windows 10 & 11 (64-bit).
*   **Runtime:** Native `.pyd` (Windows DLL) obfuscation engine.
*   **Setup:** Optimized for Windows threading and file paths.

---

## 🚀 Key Features

-   **High-Speed Transcription:** Utilizes CTranslate2 for up to 4x faster audio analysis.
-   **Intelligent Taming (V6):** Optimized segment splitting to prevent "fast subtitles" and ensure 100% Arabic output.
-   **Word-Level Precision:** Syllable-accurate timing for professional-grade results.
-   **Privacy & Stealth:** Industrial-strength obfuscation (MITRE T1027) protects API keys and core logic.
-   **Arabic RTL Support:** Native handling of Right-to-Left text with correct Unicode rendering.

---

## 🛠️ Global Quick Start

1.  **Select your platform** from the folders above.
2.  **Install FFmpeg** (Ensuring it's in your system PATH).
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the application:**
    ```bash
    python main.py
    ```

---

## 🔒 Security Context (MITRE ATT&CK)
This project implements advanced defensive coding techniques:
*   **Technique [T1027]:** Code Obfuscation at the binary level.
*   **Logic Isolation:** Critical API management and license logic are encrypted within the runtime engine.

---

Developed with ❤️ by **@LIMEDARKK**
*Empowering content creators with AI-driven localization.*
