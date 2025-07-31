import os
from modules.cookie_checker import get_username_from_cookie
from modules.normal_chat import start_normal_chat
from modules.e2ee_chat import start_e2ee_chat

def load_cookie():
    try:
        with open('cookies.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("❌ 'cookies.txt' file not found.")
        return None

def main():
    os.system("clear")
    print("⚡ Facebook Chat Auto Sender ⚡\n")

    cookie = load_cookie()
    if not cookie:
        return

    username = get_username_from_cookie(cookie)
    if not username:
        print("❌ Invalid Cookie!")
        return

    print(f"✔ Cookie Valid! Logged in as: {username}\n")

    print("[1] Normal Chat Conversation")
    print("[2] End-to-End Encrypted (E2EE) Conversation")

    choice = input("Choose Option [1/2]: ").strip()

    if choice == "1":
        start_normal_chat(cookie)
    elif choice == "2":
        print("Starting E2EE Chat Mode...                              Coming Soon!")
        start_e2ee_chat(cookie)
    else:
        print("❌ Invalid Choice!")

if __name__ == "__main__":
    main()
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
