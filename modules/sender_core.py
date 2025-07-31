# modules/sender_core.py

import requests
import time
from modules.logger import log_info

def send_messages(cookies, message_file, e2ee=False):
    try:
        with open(message_file, "r", encoding="utf-8") as f:
            messages = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        log_info(f"{message_file} not found!", "error")
        return

    chat_id = input("Enter Chat Thread ID: ").strip()
    delay = int(input("Delay between messages (in seconds): ").strip())

    index = 0
    while True:
        for cookie in cookies:
            message = messages[index % len(messages)]
            prefix = "[E2EE]" if e2ee else "[CHAT]"
            full_message = f"{prefix} {message}"
            success = simulate_send(chat_id, full_message, cookie, e2ee)
            if success:
                log_info(f"Sent: {full_message}", "success")
            else:
                log_info("Failed to send", "warn")
            time.sleep(delay)
            index += 1

def simulate_send(chat_id, message, cookie, e2ee):
    # Fake simulation (you’ll replace this with your real request)
    headers = {
        "cookie": cookie,
        "user-agent": "Mozilla/5.0"
    }
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        # Placeholder request, replace with real Facebook chat URL and params
        response = requests.post("https://www.facebook.com/api/chat", headers=headers, data=payload)
        return response.status_code == 200
    except:
        return False
