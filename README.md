# ⚡ Lightning - Linux AI Assistant

**Lightning** is a lightweight AI-powered voice and text assistant designed for Linux users. It runs system commands, answers queries using an offline LLM (LLaMA 3), and simplifies terminal interactions — all from your voice or keyboard.

> 🧠 Built for hackers, students, and automation lovers. Works even without internet.

---

## ✨ Features

- 🎤 Voice or keyboard command input
- 📦 `install`, `check`, `run` system commands via voice/text
- 🤖 Offline AI answers using [LLaMA 3 via Ollama](https://ollama.com/library/llama3)
- 🧠 Remembers context and provides intelligent replies
- 🪶 Runs on low-resource systems (16GB RAM + 32GB storage)
- 💬 Human-like voice replies via `pyttsx3`
- 🔒 Local-first: no external cloud calls needed

---

## 🖥️ Requirements

- Linux (tested on Kali, Debian-based distros)
- Python 3.10+
- Virtual environment (recommended)
- [Ollama](https://ollama.com) installed with `llama3` pulled

---

## 🔧 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/Lightning.git
cd Lightning

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Pull LLaMA 3 model
ollama run llama3
