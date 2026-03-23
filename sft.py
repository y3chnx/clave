from datasets import load_dataset
from torch.utils.data import IterableDataset, DataLoader
import torch.optim as optim
from transformers import get_cosine_schedule_with_warmup
import os

# ---- SFT Data load ----
sft_raw = load_dataset(
    "json",
    data_files=f"hf://datasets/{DATASET_REPO}/sft.jsonl",
    split="train",
    streaming=True,
)

# ---- Format Functions ----
def format_sft_sample(example):
    conversations = example.get("conversations", [])
    parts = []
    for msg in conversations:
        role    = msg.get("role", "")
        content = msg.get("content", "")
        if role == "system":
            parts.append(f"<|im_start|>system\n{content}<|im_end|>")
        elif role == "user":
            parts.append(f"<|im_start|>user\n{content}<|im_end|>")
        elif role == "assistant":
            parts.append(f"<|im_start|>assistant\n{content}<|im_end|>")
    return "\n".join(parts) + tokenizer.eos_token

# ---- Dataset ----
class SFTDataset(IterableDataset):
    def __init__(self, dataset, tokenizer, max_len=1024):
        self.dataset   = dataset
        self.tokenizer = tokenizer
        self.max_len   = max_len

    def __iter__(self):
        for example in self.dataset:
            text    = format_sft_sample(example)
            encoded = self.tokenizer(text, truncation=True,
                                     max_length=self.max_len, return_tensors="pt")
            ids = encoded["input_ids"].squeeze(0)
            yield {"input_ids": ids, "labels": ids.clone(),
                   "attention_mask": torch.ones_like(ids)}

# ---- Collate ----
def collate_fn(batch):
    max_len   = max(b["input_ids"].shape[0] for b in batch)
    input_ids = torch.zeros(len(batch), max_len, dtype=torch.long)
    labels    = torch.full((len(batch), max_len), -100, dtype=torch.long)
    attn_mask = torch.zeros(len(batch), max_len, dtype=torch.long)
    for i, b in enumerate(batch):
        l = b["input_ids"].shape[0]
        input_ids[i, :l] = b["input_ids"]
        labels[i, :l]    = b["labels"]
        attn_mask[i, :l] = b["attention_mask"]
    return {"input_ids": input_ids, "labels": labels, "attention_mask": attn_mask}

# ---- Hyperparameters ----
MAX_STEPS  = 10000
WARMUP     = 500
BATCH_SIZE = 1
GRAD_ACCUM = 4
SAVE_EVERY = 2000
LOG_EVERY  = 100
SFT_DIR    = "/kaggle/working/sft_ckpt" #Change it to your sft dir. I used Kaggle Notebook.
os.makedirs(SFT_DIR, exist_ok=True)

sft_loader = DataLoader(SFTDataset(sft_raw, tokenizer), batch_size=BATCH_SIZE,
                        num_workers=0, pin_memory=True, collate_fn=collate_fn)
optimizer  = optim.AdamW(model.parameters(), lr=2e-5, betas=(0.9, 0.95), weight_decay=0.01)
scheduler  = get_cosine_schedule_with_warmup(optimizer, WARMUP, MAX_STEPS)

model.train()
step = 0; total_loss = 0.0
optimizer.zero_grad()

print(f"{MAX_STEPS} Steps Training Started")

for batch in sft_loader:
    if step >= MAX_STEPS:
        break

    input_ids = batch["input_ids"].to(device)
    labels    = batch["labels"].to(device)
    attn_mask = batch["attention_mask"].to(device)

    with torch.amp.autocast('cuda', dtype=torch.bfloat16):
        loss = model(input_ids=input_ids, attention_mask=attn_mask,
                     labels=labels).loss / GRAD_ACCUM

    loss.backward()
    total_loss += loss.item() * GRAD_ACCUM
    step += 1

    if step % GRAD_ACCUM == 0:
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        scheduler.step()
        optimizer.zero_grad()

    if step % LOG_EVERY == 0:
        avg = total_loss / LOG_EVERY
        print(f"Step {step:>5} | Loss: {avg:.4f} | LR: {scheduler.get_last_lr()[0]:.2e}")
        total_loss = 0.0

    if step % SAVE_EVERY == 0:
        model.save_pretrained(f"{SFT_DIR}/step-{step}")
        tokenizer.save_pretrained(f"{SFT_DIR}/step-{step}")
        try:
            model.push_to_hub(SFT_REPO, commit_message=f"SFT step {step}", token=HF_TOKEN)
            tokenizer.push_to_hub(SFT_REPO, token=HF_TOKEN)
            print(f"HF Hub Saved → {SFT_REPO}")
        except Exception as e:
            print(f"HF push Failed: {e}")

# Save
model.save_pretrained(f"{SFT_DIR}/final")
tokenizer.save_pretrained(f"{SFT_DIR}/final")
model.push_to_hub(SFT_REPO, commit_message="Final SFT model", token=HF_TOKEN)
tokenizer.push_to_hub(SFT_REPO, token=HF_TOKEN)
print("SFT Success!")