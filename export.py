from huggingface_hub import HfApi, create_repo
import os

EXPORT_DIR = "/kaggle/working/model_export"
GGUF_DIR   = "/kaggle/working/gguf_output"
os.makedirs(EXPORT_DIR, exist_ok=True)
os.makedirs(GGUF_DIR, exist_ok=True)

# Model Saving
print("Model Saving...")
model.save_pretrained(EXPORT_DIR)
tokenizer.save_pretrained(EXPORT_DIR)

# llama.cpp Install
!git clone https://github.com/ggerganov/llama.cpp /kaggle/working/llama.cpp -q
!pip install -q -r /kaggle/working/llama.cpp/requirements.txt

# F16 Converting
print("GGUF 변환 중...")
!python /kaggle/working/llama.cpp/convert_hf_to_gguf.py \
    {EXPORT_DIR} \
    --outfile {GGUF_DIR}/clave-f16.gguf \
    --outtype f16

# Q4_K_M Quantization
print("doing quantization...")
!cd /kaggle/working/llama.cpp && make quantize -j4 -s
!/kaggle/working/llama.cpp/quantize \
    {GGUF_DIR}/clave-f16.gguf \
    {GGUF_DIR}/clave-Q4_K_M.gguf \
    Q4_K_M

# File size Check
print("\nCreated File:")
for f in os.listdir(GGUF_DIR):
    s = os.path.getsize(f"{GGUF_DIR}/{f}") / 1e9
    print(f"   {f}: {s:.2f} GB")

# HF Hub Upload
api = HfApi()
create_repo(GGUF_REPO, repo_type="model", exist_ok=True, token=HF_TOKEN)

for filename in os.listdir(GGUF_DIR):
    if not filename.endswith(".gguf"):
        continue
    filepath = f"{GGUF_DIR}/{filename}"
    size_gb  = os.path.getsize(filepath) / 1e9
    print(f"\nUploading: {filename} ({size_gb:.2f} GB)...")
    api.upload_file(
        path_or_fileobj=filepath,
        path_in_repo=filename,
        repo_id=GGUF_REPO,
        repo_type="model",
        token=HF_TOKEN,
    )
    print(f"{filename} upload success!")

print(f"\nPerfect!!")
print(f"🌐 https://huggingface.co/{GGUF_REPO}")