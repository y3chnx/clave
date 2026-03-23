!pip install -q transformers datasets accelerate huggingface_hub sentencepiece

from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login
import torch, os

# ----Settings----
HF_TOKEN      = ""  #Hugging Face Tokens
HF_USERNAME   = ""  #Hugging Face Username
MODEL_NAME    = ""  #Model Name for your llm
SFT_REPO      = f"{HF_USERNAME}/{MODEL_NAME}-sft"
GGUF_REPO     = f"{HF_USERNAME}/{MODEL_NAME}-GGUF"
DATASET_REPO  = ""  #Your Hugging Face Dataset Repository

login(token=HF_TOKEN)

print("Loading Model...")
model     = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B")
tokenizer.pad_token = tokenizer.eos_token

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model  = model.to(device)
model.gradient_checkpointing_enable()
model.config.use_cache = False

total = sum(p.numel() for p in model.parameters())
print(f"{total/1e9:.2f}B load success")
print(f"GPU: {torch.cuda.get_device_name(0)}")