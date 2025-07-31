import requests
import json
import time

def send_e2ee_message(thread_id, message, cookies):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
        }

        data = {
            "message": message,
            "thread_id": thread_id,
            "__a": 1
        }

        response = requests.post(
            "https://www.facebook.com/messaging/send/",
            headers=headers,
            data=data,
            cookies=cookies
        )

        if response.status_code == 200 and "error" not in response.text.lower():
            return True
        else:
            print("\n[❌] Failed to send message!")
            print("[🔎] HTTP Status:", response.status_code)
            try:
                print("[📄] Response:", response.json())
            except:
                print("[📄] Raw Response:", response.text[:200])  # Limit output
            return False

    except Exception as e:
        print(f"\n[⚠️] Exception occurred: {str(e)}")
        return False
