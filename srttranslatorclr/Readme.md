# SRT Translator CLI

A fast, interactive command-line tool to translate subtitle files (`.srt` / `.vtt`) into Arabic using the **Zhipu AI API**.

## Features

- 🔑 API key management (save/load from config)
- 📁 Folder-based batch translation
- ⚡ Parallel processing with adjustable speed levels
- 📊 Real-time progress with ETA and elapsed time
- ✅ Final summary of successful/failed translations

## Requirements

- Python 3.8+
- Windows x86_64 **or** Linux x86_64

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python srttranslator.py
```

Follow the interactive prompts to:
1. Enter your Zhipu AI API key
2. Select the folder containing subtitle files
3. Choose translation speed
4. Start translating!

## Notes

- Supports `.srt` and `.vtt` subtitle formats
- Output files are saved alongside the originals with a language suffix
- Compatible with **Windows** and **Linux** (x86_64)
