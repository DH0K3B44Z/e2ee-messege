import os
import time
import requests
from modules.cookie_checker import get_username_from_cookie
from modules.e2ee_chat import start_e2ee_chat
from modules.normal_chat import start_normal_chat

def clear():
    os.system("clear")

def banner():
    print("""
╔═════════════════════════════════════╗
║      ⚡ Facebook Messenger Tool ⚡    ║
╠═════════════════════════════════════╣
║  [1] Normal Chat Conversation       ║
║  [2] End-to-End Encrypted (E2EE)    ║
╚═════════════════════════════════════╝
""")

def get_cookie():
    if not os.path.exists("cookie.txt"):
        open("cookie.txt", "w").close()
        print("❗ Please paste your Facebook cookie in cookie.txt")
        exit()
    with open("cookie.txt", "r") as f:
        return f.read().strip()

def main():
    clear()
    print("🔍 Validating cookie...")
    cookie = get_cookie()
    username = get_username_from_cookie(cookie)
    if not username:
        print("❌ Invalid or expired cookie. Please update cookie.txt")
        return
    print(f"✔ Cookie Valid! Logged in as: {username}\n")
    time.sleep(1)

    banner()
    opt = input("📩 Choose Option [1/2]: ").strip()
    if opt == "1":
        start_normal_chat(cookie)
    elif opt == "2":
        thread_id = input("🔑 Enter E2EE Chat Thread ID: ").strip()
        print("📤 Starting E2EE Chat Mode...")
        start_e2ee_chat(cookie, thread_id)
    else:
        print("❗ Invalid option.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⛔ Exiting.")
