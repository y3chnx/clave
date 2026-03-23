<img src="banner.png">

> The open source Large Language Model assistance

![License](https://img.shields.io/badge/license-MIT-green) ![Language](https://img.shields.io/badge/language-Python-yellow) ![Framework](https://img.shields.io/badge/framework-Pytorch-orange) ![GitHub](https://img.shields.io/badge/GitHub-y3chnx/clave-black?logo=github)

## 📋 Table of Contents

- Features
- LLM Informations
- Installation
- Usage
- Requirements
- SFT training Guide

## ℹ️ Project Information

- **👤 Author:** y3chnx
- **📄 License:** MIT
- **📂 Repository:** [https://github.com/y3chnx/clave](https://github.com/y3chnx/clave)
- **🏷️ Project Type:** Large Language Model

<div align="center">
_________________________________<br>
⚠️WARNING⚠️
<br>
Since Clave is a very small model and made by a single developer, the information that it gives can not be accurate. Do not depend on **Clave**.<br>
_________________________________
<div align="left">
  
## Features

Clave can Assist users in any ways!! It can speak, write, code, entertain, etc.

## LLM Informations

I used _Qwen/Qwen2.5-0.5B_ pretrained model for **Clave**. You can see Qwen2.5-0.5B model [here](https://huggingface.co/Qwen/Qwen2.5-0.5B) <br>
I used _OpenHermes-2.5_ SFT dataset to make my own SFT dataset. You can see OpenHermes2.5 [here](https://huggingface.co/datasets/teknium/OpenHermes-2.5) and you can see my dataset over [here](https://huggingface.co/datasets/y3chnx/clave_data/tree/main)
<br>
<br>
**These are the loss and steps for Clave:**<br>
Step   100 | Loss: 1.9280 | LR: 1.00e-06<br>
Step   200 | Loss: 1.8363 | LR: 2.00e-06<br>
Step   300 | Loss: 1.7854 | LR: 3.00e-06<br>
Step   400 | Loss: 1.5902 | LR: 4.00e-06<br>
Step   500 | Loss: 1.5961 | LR: 5.00e-06<br>
Step   600 | Loss: 1.3348 | LR: 6.00e-06<br>
Step   700 | Loss: 1.4965 | LR: 7.00e-06<br>
Step   800 | Loss: 1.4779 | LR: 8.00e-06<br>
Step   900 | Loss: 1.4050 | LR: 9.00e-06<br>
Step  1000 | Loss: 1.4053 | LR: 1.00e-05<br>
Step  1100 | Loss: 1.3803 | LR: 1.10e-05<br>
Step  1200 | Loss: 1.2000 | LR: 1.20e-05<br>
Step  1300 | Loss: 1.2033 | LR: 1.30e-05<br>
Step  1400 | Loss: 1.5076 | LR: 1.40e-05<br>
Step  1500 | Loss: 1.2009 | LR: 1.50e-05<br>
Step  1600 | Loss: 1.1581 | LR: 1.60e-05<br>
Step  1700 | Loss: 1.1279 | LR: 1.70e-05<br>
Step  1800 | Loss: 1.1493 | LR: 1.80e-05<br>
Step  1900 | Loss: 1.2055 | LR: 1.90e-05<br>
Step  2000 | Loss: 1.2736 | LR: 2.00e-05<br>
Step  2100 | Loss: 1.0362 | LR: 2.00e-05<br>
Step  2200 | Loss: 1.3371 | LR: 2.00e-05<br>
Step  2300 | Loss: 1.2108 | LR: 2.00e-05<br>
Step  2400 | Loss: 1.0655 | LR: 2.00e-05<br>
Step  2500 | Loss: 1.0744 | LR: 2.00e-05<br>
Step  2600 | Loss: 1.2879 | LR: 2.00e-05<br>
Step  2700 | Loss: 1.2418 | LR: 2.00e-05<br>
Step  2800 | Loss: 1.0000 | LR: 2.00e-05<br>
Step  2900 | Loss: 1.1651 | LR: 2.00e-05<br>
Step  3000 | Loss: 1.0862 | LR: 2.00e-05<br>
Step  3100 | Loss: 1.4159 | LR: 2.00e-05<br>
Step  3200 | Loss: 1.1334 | LR: 2.00e-05<br>
Step  3300 | Loss: 1.0738 | LR: 1.99e-05<br>
Step  3400 | Loss: 1.1301 | LR: 1.99e-05<br>
Step  3500 | Loss: 1.1340 | LR: 1.99e-05<br>
Step  3700 | Loss: 1.3415 | LR: 1.99e-05<br>
Step  3800 | Loss: 1.1623 | LR: 1.99e-05<br>
Step  3900 | Loss: 1.1985 | LR: 1.99e-05<br>
Step  4000 | Loss: 1.1380 | LR: 1.99e-05<br>
Step  4100 | Loss: 1.1319 | LR: 1.98e-05<br>
Step  4200 | Loss: 1.0780 | LR: 1.98e-05<br>
Step  4300 | Loss: 1.1658 | LR: 1.98e-05<br>
Step  4400 | Loss: 1.1715 | LR: 1.98e-05<br>
Step  4500 | Loss: 1.0786 | LR: 1.98e-05<br>
Step  4600 | Loss: 1.1585 | LR: 1.98e-05<br>
Step  4700 | Loss: 1.0313 | LR: 1.98e-05<br>
Step  4800 | Loss: 1.0327 | LR: 1.97e-05<br>
Step  4900 | Loss: 1.1474 | LR: 1.97e-05<br>
Step  5000 | Loss: 1.0770 | LR: 1.97e-05<br>
Step  5100 | Loss: 1.1415 | LR: 1.97e-05<br>
Step  5200 | Loss: 1.1242 | LR: 1.97e-05<br>
Step  5300 | Loss: 1.2055 | LR: 1.96e-05<br>
Step  5400 | Loss: 1.0293 | LR: 1.96e-05<br>
Step  5500 | Loss: 0.9618 | LR: 1.96e-05<br>
Step  5600 | Loss: 1.1262 | LR: 1.96e-05<br>
Step  5700 | Loss: 1.1229 | LR: 1.95e-05<br>
Step  5800 | Loss: 1.5038 | LR: 1.95e-05<br>
Step  5900 | Loss: 1.0221 | LR: 1.95e-05<br>
Step  6000 | Loss: 1.0904 | LR: 1.95e-05<br>
Step  6100 | Loss: 0.9646 | LR: 1.94e-05<br>
Step  6200 | Loss: 1.2279 | LR: 1.94e-05<br>
Step  6300 | Loss: 1.2332 | LR: 1.94e-05<br>
Step  6400 | Loss: 1.0834 | LR: 1.93e-05<br>
Step  6500 | Loss: 1.1939 | LR: 1.93e-05<br>
Step  6600 | Loss: 1.1774 | LR: 1.93e-05<br>
Step  6700 | Loss: 1.0380 | LR: 1.93e-05<br>
Step  6800 | Loss: 1.1954 | LR: 1.92e-05<br>
Step  6900 | Loss: 1.0722 | LR: 1.92e-05<br>
Step  7000 | Loss: 1.3323 | LR: 1.92e-05<br>
Step  7100 | Loss: 1.2450 | LR: 1.91e-05<br>
Step  7200 | Loss: 1.1012 | LR: 1.91e-05<br>
Step  7300 | Loss: 1.2580 | LR: 1.91e-05<br>
Step  7400 | Loss: 1.1068 | LR: 1.90e-05<br>
Step  7500 | Loss: 1.1131 | LR: 1.90e-05<br>
Step  7600 | Loss: 1.2079 | LR: 1.89e-05<br>
Step  7700 | Loss: 0.9763 | LR: 1.89e-05<br>
Step  7800 | Loss: 0.9920 | LR: 1.89e-05<br>
Step  7900 | Loss: 1.1431 | LR: 1.88e-05<br>
Step  8000 | Loss: 1.2436 | LR: 1.88e-05<br>
Step  8100 | Loss: 1.1506 | LR: 1.88e-05<br>
Step  8200 | Loss: 1.1598 | LR: 1.87e-05<br>
Step  8300 | Loss: 1.1867 | LR: 1.87e-05<br>
Step  8400 | Loss: 1.0443 | LR: 1.86e-05<br>
Step  8500 | Loss: 1.0803 | LR: 1.86e-05<br>
Step  8600 | Loss: 1.0515 | LR: 1.85e-05<br>
Step  8700 | Loss: 1.2538 | LR: 1.85e-05<br>
Step  8800 | Loss: 1.2145 | LR: 1.85e-05<br>
Step  8900 | Loss: 1.1102 | LR: 1.84e-05<br>
Step  9000 | Loss: 1.0160 | LR: 1.84e-05<br>
Step  9100 | Loss: 1.0920 | LR: 1.83e-05<br>
Step  9200 | Loss: 1.1582 | LR: 1.83e-05<br>
Step  9300 | Loss: 1.0306 | LR: 1.82e-05<br>
Step  9400 | Loss: 1.0571 | LR: 1.82e-05<br>
Step  9500 | Loss: 1.0446 | LR: 1.81e-05<br>
Step  9600 | Loss: 1.0949 | LR: 1.81e-05<br>
Step  9700 | Loss: 1.1913 | LR: 1.80e-05<br>
Step  9800 | Loss: 1.0932 | LR: 1.80e-05<br>
Step  9900 | Loss: 1.1682 | LR: 1.79e-05<br>
Step 10000 | Loss: 1.0923 | LR: 1.79e-05<br>


## Installation

- First, you need to install Python on your computer. You can download Python with [this](https://www.python.org/downloads/). 
- Next, you need to get clave-f16.gguf from my Hugging Face. You can click [this](https://huggingface.co/y3chnx/clave-GGUF/resolve/main/clave-f16.gguf) to download the model.
- Then, download this whole GitHub repository as a zip file.
- Go to the folder called [clave_cli] and make [models] folder inside. 
- When you are done with that, put your model file(clave_f16.gguf) inside the [models] folder.
- Finally, install all the dependencies and run [main.py]. You can use the command to run:
``` python main.py```

## Usage

You can talk with it:
<br> <img src="talk.png">
<br> 
You can make it write something:
<br> <img src="write.png">
<br>
<br>You can make it code:
<br> <img src="code.png">

## Requirements

Python 3.11 or Higher <br>
llama-cpp-python

## SFT Training Guide

If you want to try SFT training as I did, you can run my three Python files in your virtual computer (Google Collab or Kaggle; I used Kaggle Notebook). 
<Br>You need to run in this order:
<br> <div align="center">
[Setting.py](setting.py)
<br>⬇️<br>
[sft.py](sft.py)
<br>⬇️<br>
[export.py](export.py)
<br> <div align="left">
There might be missing information(private information) that you need to fill out on the code. (You need a Hugging Face Token to do this job.)
<br>
<Br> <div align="center">
