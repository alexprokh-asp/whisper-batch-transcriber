# Whisper GPU Batch Transcriber

GPU-accelerated local batch audio transcription tool using Faster Whisper and NVIDIA CUDA.

It converts multiple MP3 files from an input folder into clean text files in an output folder.

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
