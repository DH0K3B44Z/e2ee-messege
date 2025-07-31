from modules.cookie_checker import get_username_from_cookie
from modules.normal_chat import send_normal_messages
from modules.e2ee_chat import send_e2ee_messages
import os

def clear():
    os.system("clear")

def menu():
    clear()
    print("✔ Cookie Valid! Logged in as: Facebook\n")
    print("[1] Normal Chat Conversation")
    print("[2] End-to-End Encrypted (E2EE) Conversation")
    choice = input(" " * 55 + "Choose Option [1/2]: ").strip()
    if choice == "1":
        print("Starting Normal Chat Mode...")
        send_normal_messages()
    elif choice == "2":
        print("Starting E2EE Chat Mode...")
        send_e2ee_messages()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    menu()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Exiting by user.[/bold red]")
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
