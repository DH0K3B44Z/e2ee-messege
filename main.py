import os
from rich.console import Console
from rich.panel import Panel
from modules.cookie_checker import check_and_print_username
from modules.messenger import start_normal_chat, start_e2ee_chat

console = Console()

def show_logo():
    path = "assets/saiim_logo.txt"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            logo = f.read()
        console.print(Panel.fit(logo, title="[bold green]SAIIM MESSENGER", border_style="bold blue"))
    else:
        console.print("[bold red]Logo file missing![/bold red]")

def show_menu():
    console.print("\n[bold cyan][1][/bold cyan] Normal Chat Conversation")
    console.print("[bold cyan][2][/bold cyan] End-to-End Encrypted (E2EE) Conversation")
    return console.input("\n[bold yellow]Choose Option [1/2]: [/bold yellow]").strip()

def main():
    os.system("clear" if os.name == "posix" else "cls")
    show_logo()

    if not check_and_print_username("cookies.txt"):
        return

    choice = show_menu()
    if choice == '1':
        start_normal_chat()
    elif choice == '2':
        start_e2ee_chat()
    else:
        console.print("[red]Invalid option. Exiting...[/red]")

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
