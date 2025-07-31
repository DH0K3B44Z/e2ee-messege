# modules/normal_chat.py

from modules.sender_core import send_messages
from modules.logger import log_info
from modules.cookie_utils import load_cookies

def start():
    cookies = load_cookies()
    if not cookies:
        log_info("No valid cookies found!", "error")
        return
    send_messages(
        cookies=cookies,
        message_file="messages/normal.txt",
        e2ee=False
    )
