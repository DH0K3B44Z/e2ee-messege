import requests
import time
import sys
import os
import json

# --------- COOKIE LOADER FUNCTION ---------
def load_cookie():
    try:
        with open("cookie.txt", "r") as f:
            raw = f.read().strip()
            cookies = {}
            for item in raw.split(";"):
                if "=" in item:
                    key, value = item.strip().split("=", 1)
                    cookies[key] = value
            return cookies
    except FileNotFoundError:
        print("🚫 cookie.txt file not found.")
        sys.exit(1)

# --------- COOKIE CHECKER FUNCTION ---------
def check_cookie(cookies):
    try:
        response = requests.get(
            "https://www.facebook.com/me?__a=1",
            cookies=cookies,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )
        if response.status_code == 200:
            data = json.loads(response.text.replace("for (;;);", ""))
            name = data.get("name") or data.get("user", {}).get("name") or "Unknown"
            uid = data.get("id") or data.get("user", {}).get("id") or "N/A"
            print(f"\n✅ Cookie valid: Logged in as {name} (UID: {uid})\n")
            return True
        else:
            print("❌ Cookie check failed. HTTP", response.status_code)
            return False
    except Exception as e:
        print("❌ Cookie check error:", str(e))
        return False

# --------- MESSAGE SENDER FUNCTION ---------
def send_message(thread_id, message, cookies, is_e2ee=False):
    url = "https://www.facebook.com/api/graphql/" if is_e2ee else "https://www.facebook.com/messages/send/"
    payload = {
        "id": thread_id,
        "message": message,
        "timestamp": str(int(time.time() * 1000))
    }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, cookies=cookies, json=payload)
        if response.status_code == 200:
            print(f"✅ Message sent successfully at {time.strftime('%H:%M:%S')}")
        else:
            print("❌ Failed to send message. HTTP", response.status_code)
    except Exception as e:
        print("❌ Error sending message:", str(e))

# --------- MAIN FUNCTION ---------
def main():
    os.system("clear")
    print("🔐 Facebook Auto Messenger Tool - By SAIIM 🔐\n")

    cookies = load_cookie()
    if not check_cookie(cookies):
        print("🚫 Invalid Facebook cookie. Please fix your cookie.txt file.")
        sys.exit(1)

    print("[1] Normal Chat Conversation")
    print("[2] End-to-End Encrypted (E2EE) Conversation")
    choice = input("                                                        Choose Option [1/2]: ").strip()

    if choice not in ["1", "2"]:
        print("❌ Invalid option.")
        return

    is_e2ee = choice == "2"
    thread_id = input("\nEnter {} Chat Thread ID: ".format("E2EE" if is_e2ee else "Normal")).strip()

    if not thread_id.isdigit():
        print("❌ Invalid thread ID.")
        return

    print("💬 Messaging started... Press Ctrl+C to stop.\n")

    try:
        with open("messages.txt", "r", encoding="utf-8") as f:
            messages = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("❌ messages.txt not found.")
        return

    index = 0
    while True:
        message = messages[index]
        send_message(thread_id, message, cookies, is_e2ee=is_e2ee)
        index = (index + 1) % len(messages)
        time.sleep(60)  # 60 second delay
except KeyboardInterrupt:
        print("\n🛑 Messaging stopped by user.")

# --------- ENTRY POINT ---------
if __name__ == "__main__":
    main()
def main():
    os.system("clear" if os.name == "posix" else "cls")
    show_logo()

    if not check_cookie():
        return

    choice = show_menu()

    if choice == '1':
        normal_chat.start()
    elif choice == '2':
        e2ee_chat.start()
    else:
        console.print("[red]Invalid option! Exiting.[/red]")

if __name__ == "__main__":
    main()
