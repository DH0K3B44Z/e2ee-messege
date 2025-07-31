import time
import random

def load_messages(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def load_thread(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()

def simulate_typing(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(random.uniform(0.05, 0.15))
    print()

def delay():
    time.sleep(random.randint(50, 60))  # Change delay range here
