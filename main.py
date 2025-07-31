import os
from rich.console import Console
from rich.panel import Panel
from modules import normal_chat, e2ee_chat, cookie_utils

console = Console()

def show_logo():
    try:
        with open("assets/saiim_logo.txt", "r", encoding="utf-8") as f:
            logo = f.read()
        console.print(Panel.fit(logo, title="[bold green]SAIIM MESSENGER", border_style="bold blue"))
    except FileNotFoundError:
        console.print("[red]Logo file not found! Skipping logo...[/red]")

def check_cookie_and_show_user():
    if not os.path.exists("cookies.txt"):
        console.print("[red]cookies.txt file not found![/red]")
        return False

    try:
        with open("cookies.txt", "r", encoding="utf-8") as f:
            cookie = f.read().strip()
            if not cookie:
                console.print("[red]Cookie file is empty![/red]")
                return False

        username = cookie_utils.get_username(cookie)
        if username:
            console.print(f"[green]✔ Cookie Valid! Logged in as:[/green] [bold cyan]{username}[/bold cyan]")
            return True
        else:
            console.print("[red]❌ Invalid or expired cookie.[/red]")
            return False
    except Exception as e:
        console.print(f"[red]Error reading cookie: {e}[/red]")
        return False

def show_menu():
    console.print("\n[bold cyan][1][/bold cyan] Normal Chat Conversation")
    console.print("[bold cyan][2][/bold cyan] End-to-End Encrypted (E2EE) Conversation")
    choice = console.input("\n[bold yellow]Choose Option [1/2]: [/bold yellow]")
    return choice.strip()

def main():
    os.system("clear" if os.name == "posix" else "cls")
    show_logo()

    if not check_cookie_and_show_user():
        return

    choice = show_menu()

    if choice == '1':
        normal_chat.start()
    elif choice == '2':
        e2ee_chat.start()
    else:
        console.print("[red]Invalid option! Exiting.[/red]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Exiting by user...[/red]")
