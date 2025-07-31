# modules/logger.py

from datetime import datetime

def log_message(sender, message):
    with open("message_log.txt", "a", encoding="utf-8") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{now}] {sender}: {message}\n")
