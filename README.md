# FrameDrop

A lightweight tool to reduce the frame rate of video files using FFmpeg.

## Features

- Reduce video FPS (e.g., from 60 → 15)
- Command-line interface
- Easily extendable to support other video utilities

## Requirements

- Python 3.7+
- [FFmpeg](https://ffmpeg.org/download.html) installed and in your system PATH

## Setup (Recommended: Virtual Environment)

```bash
# Clone or download this repo
cd framedrop

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate           # On Linux/macOS
# OR
venv\Scripts\activate.bat          # On Windows CMD
# OR
.\venv\Scripts\Activate.ps1        # On Windows PowerShell

# Install dependencies
pip install -r requirements.txt
```
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
