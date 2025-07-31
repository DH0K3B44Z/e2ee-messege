import requests
import re

def get_username_from_cookie(cookie):
    headers = {
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0',
    }
    try:
        res = requests.get('https://www.facebook.com', headers=headers)
        name = re.findall('"name":"(.*?)"', res.text)
        if name:
            return name[0]
    except:
        return None
