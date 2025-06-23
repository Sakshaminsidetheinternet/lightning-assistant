#!/bin/bash

echo "⚡ Setting up Lightning AI Assistant..."

# Update system
sudo apt update && sudo apt install -y python3 python3-venv python3-pip ffmpeg espeak libespeak1

# Create virtual environment
cd ~/Lightning
python3 -m venv venv
source venv/bin/activate

# Install Python packages
pip install --upgrade pip
pip install -r requirements.txt

# Install Ollama if not present
if ! command -v ollama &> /dev/null; then
  echo "Installing Ollama..."
  curl -fsSL https://ollama.com/install.sh | sh
fi

# Pull LLaMA 3 model
ollama pull llama3

echo "✅ Setup complete. To start:"
echo "1. Run 'ollama run llama3' in one terminal"
echo "2. Then 'source venv/bin/activate && python3 main.py' in another"
