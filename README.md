# Whisper GPU Batch Transcriber (Local)

GPU-accelerated local batch audio transcription tool using Faster Whisper and NVIDIA CUDA.
It converts multiple MP3 files from an input folder into clean text files in an output folder.

## Project Motivation

This tool was created out of practical necessity.
I regularly work with a large number of audio recordings that need to be transcribed into text. Many of these files are long (30 minutes to over 2 hours), and processing them manually or using online services quickly becomes inefficient.
Most free transcription services have strict limitations on: file size, total usage time, number of requests ...
Because of these constraints, I needed a reliable local solution that could handle batch processing without restrictions.

---

## Solution

This project is a local GPU-accelerated transcription pipeline designed to process multiple audio files automatically.

It allows:
- batch transcription of many audio files at once
- processing of both short and long recordings (including 2+ hour files)
- fully offline usage after setup
- unlimited usage without external service restrictions

The result is a simple and efficient workflow:

input audio files → GPU processing → clean text output

---

## Installation

### 1. Install Python
Download from:
`https://www.python.org/downloads/windows/`

Verify:
```bash
python --version
```

---

### 2. Install FFmpeg
Download:
`https://www.gyan.dev/ffmpeg/builds/`

Verify:
```bash
ffmpeg -version
```

---

### 3. Install CUDA Toolkit
Download:
`https://developer.nvidia.com/cuda-downloads`

Verify:
```bash
nvidia-smi
```

---

### 4. Install PyTorch (CUDA version)

Run:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

Verify:

```bash
python
```

Inside Python:

```python
import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
```

Expected:
`True` + GPU name

---

### 5. Install Faster Whisper

```bash
pip install faster-whisper
```

---

## Project Structure

```text
WhisperProject/
├── input/        # MP3 files go here
├── output/       # TXT results go here
└── transcribe.py # main script
```

---

## Usage

1. Put MP3 files into:

```text
input/
```

2. Run:

```bash
python transcribe.py
```

3. Get results in:

```text
output/
```

---

## Model behavior

**IMPORTANT: The first run downloads the Whisper model (~1–3 GB) and may take some time.**

**After the first run, everything works fully OFFLINE using local cache (no re-download needed).**

Model used in script:

```python
WhisperModel(
    "medium",
    device="cuda",
    compute_type="float16"
)
```

---

## Performance

On RTX 3050:

- ~10x faster than real-time
- 2-hour audio ≈ 10–15 minutes processing

---

## Output example

```text
input/lecture01.mp3
→ output/lecture01.txt
```

---

## Language Configuration

By default, the transcription script is configured for **Russian speech recognition**:

```python
language="ru"
```

---

## How to change language

To enable a different language mode, modify the `language` parameter in the `transcribe()` function.

### English transcription

```python
language="en"
```

### Ukrainian transcription

```python
language="uk"
```

### Automatic language detection (recommended)

To let Whisper automatically detect the language, **remove the parameter completely**:

```python
segments, info = model.transcribe(
    file_path,
    language="ru", - REMOVE!
    vad_filter=True,
    beam_size=5
)
```

---

## Notes

- Current default: **Russian (ru)**
- Automatic mode works best for mixed-language audio (RU/EN/UA)
- Removing `language` improves flexibility but may slightly increase processing time



### n8n Workflow Integration (Lecture → AI → Google Docs)

A ready-to-use n8n workflow template is included for local automation in n8n.

The workflow runs in a local n8n instance and processes lecture transcripts through an AI pipeline.

---

### What it does:

- Receives raw lecture text via webhook
- Sends the text to an AI agent for summarization and structuring
- Converts output into a formatted technical article
- Automatically creates a Google Docs document
- Fills the document using Google Docs API

---

### Pipeline:

Lecture Text → n8n Webhook → AI Summarization → Markdown Structuring → Google Docs Export

---

### Purpose:

This workflow automates conversion of long lecture transcripts into:

- structured technical documentation
- developer-friendly notes
- clean Google Docs articles for storage and sharing
