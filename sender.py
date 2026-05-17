import requests
from pathlib import Path

WEBHOOK_URL = "http://localhost:5678/webhook/a02e0239-53a6-44ce-9939-40eab1d80f1e"

file_path = Path("output/audio.txt")

if not file_path.exists():
    raise FileNotFoundError("audio.txt не найден в текущей папке")

with file_path.open("r", encoding="utf-8") as f:
    content = f.read()

payload = {
    "filename": file_path.name,
    "content": content
}

response = requests.post(WEBHOOK_URL, json=payload)

print("Status:", response.status_code)
print("Response:", response.text)