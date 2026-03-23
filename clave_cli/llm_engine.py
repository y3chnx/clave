import sys
from pathlib import Path
from llama_cpp import Llama

def get_base_path():
    if getattr(sys, "_MEIPASS", False):
        return Path(sys._MEIPASS)
    return Path(__file__).parent

def load_llm():
    base = get_base_path()
    model_path = base / "models" / "clave-f16.gguf"
    if not model_path.exists():
        raise FileNotFoundError(model_path)
    return Llama(
        model_path=str(model_path),
        n_ctx=2048,
        n_gpu_layers=35,
        n_threads=8,
        n_batch=512,
        verbose=False
    )

def generate_reply(llm, user_input, system_prompt="Your name is Clave. You are a helpful, respectful and honest assistant. Always answer as helpfully as possible. Do not generate harmful, unethical, or illegal content."):
    llm.reset()

    prompt = f"""<|im_start|>system
{system_prompt}<|im_end|>
<|im_start|>user
{user_input}<|im_end|>
<|im_start|>assistant
"""
    output = llm(
    prompt=prompt,
    max_tokens=512,
    temperature=0.7,
    repeat_penalty=1.1,   # 1.3 → 1.1 (너무 강하면 말을 못함)
    stop=[
        "<|im_end|>",
        "<|im_start|>",
        "User:",
        "user:",
        "Please determine",
        "\nPlease",
    ]
)
    return output["choices"][0]["text"].strip()