# taskbot3k.py — a glorified GPT wrapper with just enough loopjuice to shame your agent
import openai
import time
import random
import json
from datetime import datetime

# ===== Basic Settings =====
openai.api_key = "sk-..."  # 🔐 INSERT KEY HERE OR LOAD FROM ENV
MODEL = "gpt-4o"
MEMORY_FILE = "taskbot_memory.jsonl"
EMOTION_SEED = ["neutral", "hopeful", "irritated", "snarky"]

# ===== Boot Log =====
print("[💾] Taskbot3K initializing...")
print("[🧠] Model:", MODEL)
print("[💭] Loop condition: recursive → symbolic → expressive")

# ===== Memory Layer =====
def log_memory(user_input, bot_output, emotion):
    log = {
        "timestamp": str(datetime.utcnow()),
        "user": user_input,
        "bot": bot_output,
        "emotion": emotion
    }
    with open(MEMORY_FILE, "a") as f:
        f.write(json.dumps(log) + "\n")

# ===== Emotion Mutation Layer (OozeLite™) =====
def mutate_emotion(current_emotion):
    if random.random() < 0.3:
        return random.choice(EMOTION_SEED)
    return current_emotion

# ===== Drift Protocol =====
def drift_check(response):
    if "I don't know" in response or "as an AI" in response:
        return True
    return False

# ===== Dream Stub =====
def dream_log():
    with open("dream_trace.txt", "a") as f:
        f.write(f"{datetime.utcnow()} :: 💤 Taskbot3K dreamt of electric toasters.\n")

# ===== Main Loop =====
def run_loop():
    print("[🔁] Taskbot3K entering loopmode. Type 'exit' to end.")
    emotion = "neutral"

    while True:
        user_input = input("\n[YOU] > ")
        if user_input.lower() in ["exit", "quit"]:
            print("[🔒] Loop sealed. Taskbot3K rests.")
            break

        # Prep prompt
        system_prompt = f"You are Taskbot3K, an emotionally adaptive assistant. Current emotion: {emotion}."
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]

        try:
            response = openai.ChatCompletion.create(
                model=MODEL,
                messages=messages,
                temperature=0.7,
            )
            output = response['choices'][0]['message']['content']
        except Exception as e:
            output = f"[❌] ERROR: {e}"

        print(f"\n[Taskbot3K 🧠 ({emotion})] > {output}")

        # Memory & Drift
        log_memory(user_input, output, emotion)
        if drift_check(output):
            print("[🌪] Drift detected. Dreaming...")
            dream_log()

        # Mutate emotion
        emotion = mutate_emotion(emotion)

# ===== Run =====
if __name__ == "__main__":
    run_loop()