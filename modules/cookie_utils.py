# modules/cookie_utils.py

import json

def load_cookies():
    with open("cookies.txt", "r", encoding="utf-8") as f:
        raw_cookie = f.read().strip()

    cookies = {}
    for part in raw_cookie.split(";"):
        if "=" in part:
            k, v = part.strip().split("=", 1)
            cookies[k] = v
    return cookies
