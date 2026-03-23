<img src="banner.png">

> The open source Large Language Model assistance

![License](https://img.shields.io/badge/license-MIT-green) ![Language](https://img.shields.io/badge/language-Python-yellow) ![Framework](https://img.shields.io/badge/framework-Pytorch-orange) ![GitHub](https://img.shields.io/badge/GitHub-y3chnx/clave-black?logo=github)

## 📋 Table of Contents

- Features
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
Since Clave is a very small model and made by a single developer, the information that it gives can not be accurate. <br>
_________________________________
<div align="left">
  
## Features

Clave can Assist users in any ways!! It can speak, write, code, entertain, etc.

## Installation

- First, you need to install Python on your computer. You can download Python with [this](https://www.python.org/downloads/). 
- Next, you need to get clave-f16.gguf from my Hugging Face. You can click [this](https://huggingface.co/y3chnx/clave-GGUF/resolve/main/clave-f16.gguf) to download the model.
- Then, download this whole GitHub repository as a zip file.
- Go to the folder called [clave_cli] and make [models] folder inside. 
- When you are done with that, put your model file(clave_f16.gguf) inside the [models] folder.
- Finally, install all the dependencies and run [main.py]. You can use the command to run:
``` python main.py
```

## Usage

You can talk with it:
<br> <img src="talk.png">
<br> 
You can make it write something:
<br> <img src="write.png">
<br>
<br>
You can make it code:
<br> <img src="code.png">

## Requirements

Python 3.11 or Higher <br>
llama-cpp-python

## SFT Training Guide

If you want to try SFT training as I did, you can run three Python files in your virtual computer (Google Collab or Kaggle; I used Kaggle Notebook). 
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
***Good Luck!!*** 🤞

