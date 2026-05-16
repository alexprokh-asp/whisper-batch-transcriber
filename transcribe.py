# ==============================
# BEGIN
# ==============================

from faster_whisper import WhisperModel
from datetime import datetime
import os
import time

# ==============================
# Configuration
# ==============================

INPUT_DIR = "input"
OUTPUT_DIR = "output"

MODEL_SIZE = "medium"

SUPPORTED_EXTENSIONS = (".mp3", ".wav", ".m4a", ".flac")

# ==============================
# Model Initialization
# ==============================

print("\nLoading Whisper model...\n")

model = WhisperModel(
    MODEL_SIZE,
    device="cuda",          # NVIDIA GPU
    compute_type="float16"  # CUDA half precision
)

print("Model loaded successfully.\n")

# ==============================
# Create Output Folder
# ==============================

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==============================
# Get Audio File List
# ==============================

files = sorted(
    [
        f for f in os.listdir(INPUT_DIR)
        if f.lower().endswith(SUPPORTED_EXTENSIONS)
    ]
)

total_files = len(files)

if total_files == 0:
    print("No audio files found in input folder.")
    exit()

# ==============================
# Transcription Function
# ==============================

def transcribe_file(file_path):

    segments, info = model.transcribe(
        file_path,
        language="ru",
        vad_filter=True,
        beam_size=5
    )

    text_parts = []

    for segment in segments:
        cleaned_text = segment.text.strip()

        if cleaned_text:
            text_parts.append(cleaned_text)

    return "\n".join(text_parts)

# ==============================
# Global Timer
# ==============================

global_start_time = time.time()

print("=" * 60)
print(f"Files found: {total_files}")
print("=" * 60)

# ==============================
# Main Loop
# ==============================

for index, file_name in enumerate(files, start=1):

    input_path = os.path.join(INPUT_DIR, file_name)

    base_name = os.path.splitext(file_name)[0]
    output_file_name = base_name + ".txt"

    output_path = os.path.join(OUTPUT_DIR, output_file_name)

    start_datetime = datetime.now()
    start_time = time.time()

    print("\n" + "-" * 60)
    print(f"[{index}/{total_files}] Processing started")
    print(f"Time: {start_datetime.strftime('%H:%M:%S')}")
    print(f"File: {file_name}")
    print("-" * 60)

    try:
        result_text = transcribe_file(input_path)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result_text)

        end_datetime = datetime.now()
        end_time = time.time()

        duration_seconds = int(end_time - start_time)

        hours = duration_seconds // 3600
        minutes = (duration_seconds % 3600) // 60
        seconds = duration_seconds % 60

        print(f"[{index}/{total_files}] Completed")
        print(f"Finished at: {end_datetime.strftime('%H:%M:%S')}")
        print(
            f"Processing time: "
            f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        )
        print(f"Saved to: {output_path}")

    except Exception as e:

        print(f"\nError processing file: {file_name}")
        print(f"Error message: {e}")

# ==============================
# Total Time
# ==============================

global_end_time = time.time()

total_duration = int(global_end_time - global_start_time)

hours = total_duration // 3600
minutes = (total_duration % 3600) // 60
seconds = total_duration % 60

print("\n" + "=" * 60)
print("All Files Processed")
print(
    f"Total runtime: "
    f"{hours:02d}:{minutes:02d}:{seconds:02d}"
)
print("=" * 60)

# ==============================
# END
# ==============================
