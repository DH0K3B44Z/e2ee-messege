import time
import random
import requests
from modules.utils import simulate_typing, log_message

def start_e2ee_chat(cookie, thread_id):
    if not thread_id:
        print("❗ Thread ID required.")
        return

    try:
        with open("messages.txt", "r", encoding="utf-8") as f:
            messages = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("❌ messages.txt not found.")
        return

    headers = {
        "cookie": cookie,
        "user-agent": "Mozilla/5.0 (Linux; Android 10)",
        "content-type": "application/x-www-form-urlencoded"
    }

    count = 0
    while True:
        for msg in messages:
            simulate_typing(msg)
            data = {
                "message": msg,
                "thread_id": thread_id,
                "__a": 1
            }
            try:
                r = requests.post("https://www.facebook.com/messages/send/", headers=headers, data=data)
                if r.status_code == 200:
                    count += 1
                    log_message(thread_id, msg, count)
                else:
                    print(f"⚠️ Failed ({r.status_code}): {msg}")
            except Exception as e:
                print(f"❌ Error: {e}")
            time.sleep(random.randint(10, 15))  # Delay between messages
