import requests
import time

def start_normal_chat(cookie):
    thread_id = input("🔗 Enter Facebook Chat Thread ID: ").strip()
    message_file = input("📄 Enter Message File Path: ").strip()

    try:
        with open(message_file, 'r', encoding='utf-8') as f:
            messages = [msg.strip() for msg in f if msg.strip()]
    except FileNotFoundError:
        print("❌ Message file not found.")
        return

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": cookie
    }

    print(f"🚀 Sending messages to Thread ID: {thread_id}...\n")
    index = 0
    while True:
        message = messages[index % len(messages)]
        payload = {
            'message': message,
            '__a': '1'
        }

        url = f"https://www.facebook.com/messages/send/?id={thread_id}"
        try:
            res = requests.post(url, headers=headers, data=payload)
            if res.status_code == 200:
                print(f"✅ Sent: {message}")
            else:
                print(f"❌ Failed: {message[:20]}... [Status: {res.status_code}]")
        except Exception as e:
            print(f"❌ Error: {e}")

        index += 1
        time.sleep(60)  # 🕒 Change delay here (default: 60 seconds)
