import requests
from bs4 import BeautifulSoup

def check_cookie():
    try:
        with open("cookies.txt", "r", encoding="utf-8") as f:
            raw = f.read().replace("\n", "").strip()
            cookies = dict(x.strip().split("=", 1) for x in raw.split(";") if "=" in x)
    except Exception as e:
        print(f"[✖] Cookie file error: {e}")
        return None

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mobile)",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        r = requests.get("https://www.facebook.com/me", cookies=cookies, headers=headers, timeout=10)
        if "home_icon" not in r.text:
            print("[✖] Invalid or expired Facebook cookie.")
            return None
    except Exception as e:
        print(f"[✖] Network error: {e}")
        return None

    # Extract user info
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.title.string if soup.title else "Unknown"
    try:
        name = title.split(" |")[0]
    except:
        name = "Unknown"

    try:
        uid = r.url.split("id=")[1].split("&")[0]
    except:
        uid = cookies.get("c_user", "Unknown")

    profile_url = f"https://www.facebook.com/{uid}"

    print(f"[✓] Cookie is valid.")
    print(f"    • Name: {name}")
    print(f"    • UID : {uid}")
    print(f"    • Profile: {profile_url}")

    return {
        "name": name,
        "uid": uid,
        "profile": profile_url
    }
