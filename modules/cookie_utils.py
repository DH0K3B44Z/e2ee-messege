# modules/cookie_utils.py

import requests
import json

def check_cookie_and_get_name(cookie_file):
    with open(cookie_file, 'r') as f:
        raw = f.read().strip()

    cookies = {}
    for item in raw.split(';'):
        if '=' in item:
            key, value = item.strip().split('=', 1)
            cookies[key] = value

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get("https://www.facebook.com/api/graphql/", params={
        "doc_id": "5300842796671573",  # known valid doc_id for profile info
        "variables": json.dumps({"scale": 3})
    }, cookies=cookies, headers=headers)

    if "Unauthorized" in res.text or res.status_code != 200:
        raise Exception("Invalid or expired cookie")

    try:
        data = res.json()
        name = data['data']['viewer']['actor']['name']
        return name
    except:
        raise Exception("Unable to fetch name from cookie")
