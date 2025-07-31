import requests
import re

def get_username_from_cookie(cookie):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Cookie": cookie
    }
    try:
        res = requests.get("https://www.facebook.com/me", headers=headers)
        if "home_icon" in res.text:
            match = re.search(r'"name":"(.*?)"', res.text)
            if match:
                return match.group(1)
            else:
                return "Facebook"
        else:
            return None
    except:
        return None
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
