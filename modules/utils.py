import sys
import time
from datetime import datetime

def simulate_typing(message):
    print("✏️ Typing: ", end="")
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def log_message(thread_id, message, count):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"✅ Sent [{count}] to {thread_id} at {now} ➤ {message}")
