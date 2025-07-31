# modules/sender_core.py

import requests
import random
import time
from modules.logger import log_message
from modules.cookie_utils import load_cookies

def send_message(thread_id, message, typing=False):
    url = f"https://www.facebook.com/messages/send/?thread_id={thread_id}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    cookies = load_cookies()
    
    payload = {
        "message": message,
        "client": "mercury"
    }

    if typing:
        delay = random.uniform(2, 5)
        for ch in message:
            time.sleep(delay / len(message))  # simulate typing
    else:
        time.sleep(random.uniform(1, 3))

    try:
        response = requests.post(url, data=payload, headers=headers, cookies=cookies)
        if response.status_code == 200:
            sender_name = cookies.get("c_user", "unknown_user")
            log_message(sender_name, message)
            return True
        else:
            return False
    except Exception:
        return False
