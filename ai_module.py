import requests

def ask_llama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False}
        )
        text = response.json()["response"].strip()
        return text if text else "⚠️ I didn't get a response from the AI."
    except Exception as e:
        return f"⚠️ LLaMA error: {e}"
