import pyttsx3
import subprocess
import os
from ai_module import ask_llama

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty('rate', 180)

def speak(text):
    print(f"Lightning: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    return input("🧠 You: ").lower().strip()

def handle_command(command):
    if "hello lightning" in command:
        speak("Hello! I am your Linux assistant, Lightning.")
        return

    elif command.startswith("install "):
        package = command.replace("install", "").strip()
        real_command = f"sudo apt install {package} -y"
        speak(f"Installing {package}...")
        subprocess.Popen(["x-terminal-emulator", "-e", f"bash -c '{real_command}; exec bash'"])

    elif command.startswith("check "):
        what = command.replace("check", "").strip()
        checks = {
            "disk": "df -h",
            "memory": "free -h",
            "internet": "ping -c 4 google.com"
        }
        if what in checks:
            real_command = checks[what]
            speak(f"Checking {what}...")
            subprocess.Popen(["x-terminal-emulator", "-e", f"bash -c '{real_command}; exec bash'"])
        else:
            speak("Sorry, I can't check that yet.")

    elif command.startswith("run "):
        real_command = command.replace("run", "").strip()
        speak(f"Executing: {real_command}")
        subprocess.Popen(["x-terminal-emulator", "-e", f"bash -c '{real_command}; exec bash'"])

    elif "sleep" in command or "stop" in command:
        speak("Goodbye. Lightning signing off.")
        exit()

    else:
        # Fallback to AI
        speak("Let me think...")
        response = ask_llama(command)
        speak(response)

# Main loop
if __name__ == "__main__":
    speak("Lightning is ready.")
    while True:
        cmd = take_command()
        handle_command(cmd)
