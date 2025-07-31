import requests
from bs4 import BeautifulSoup

def get_username(cookie):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Cookie": cookie
        }
        response = requests.get("https://www.facebook.com/me", headers=headers, timeout=10)

        if "c_user" not in cookie:
            return None

        if "login" in response.url or "checkpoint" in response.url:
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else ""
        if "Facebook" in title:
            name = title.replace(" | Facebook", "").strip()
            return name if name else "Facebook User"
        return None
    except Exception:
        return None
