import time
import os
import json
from modules.cookie_checker import get_username_from_cookie
from modules.messenger import start_messaging


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    print("""
\x1b[1;32m███████╗███████╗███████╗███████╗███████╗███████╗
╚══███╔╝██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝
  ███╔╝ █████╗  █████╗  █████╗  █████╗  █████╗  
 ███╔╝  ██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝  
███████╗███████╗███████╗███████╗███████╗███████╗
╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝
\x1b[1;34m            Facebook E2EE Messenger\x1b[1;34m            Facebook E2EE Messenger\x1b[0m
        \x1b[1;30m[    \x1b[1;30m[\x1b[1;35m@    \x1b[1;30m[\x1b[1;35m@\x1b[1;30m] Dev: Saiim | ChatGPT Enhanced Tool    \x1b[1;30m[\x1b[1;35m@\x1b[1;30m] Dev: Saiim | ChatGPT Enhanced Tool\x1b[0m
""")


def load_cookie():
    if not os.path.exists("cookie.txt"):
        print("\n\x1b[1;31m[!] cookie.txt file not found\x1b[0m")
        exit()
    with open("cookie.txt", "r") as f:
        return f.read().strip()


def load_messages():
    if not os.path.exists("messages.txt"):
        print("\n\x1b[1;31m[!] messages.txt file not found\x1b[0m")
        exit()
    with open("messages.txt", "r") as f:
        messages = [msg.strip() for msg in f if msg.strip()]
    if not messages:
        print("\n\x1b[1;31m[!] No messages found in messages.txt\x1b[0m")
        exit()
    return messages


def main():
    clear()
    banner()

    cookie = load_cookie()
    username = get_username_from_cookie(cookie)
    print(f"\n\x1b[1;32m[✓] Logged in as: \x1b[1;36m{username}\x1b[0m")

    thread_id = input("\n\x1b[1;33m[?] Enter E2EE Thread ID: \x1b[0m").strip()
    if not thread_id:
        print("\x1b[1;31m[!] Thread ID cannot be empty\x1b[0m")
        return

    try:
        delay = int(input("\x1b[1;33m[?] Delay between messages (seconds): \x1b[0m"))
    except ValueError:
        print("\x1b[1;31m[!] Invalid delay input\x1b[0m")
        return

    messages = load_messages()

    start_messaging(cookie=cookie, thread_id=thread_id, messages=messages, delay=delay)


if __name__ == "__main__":
    main()
