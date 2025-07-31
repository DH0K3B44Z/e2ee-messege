import os
import requests
from rich.console import Console
from rich.panel import Panel
from modules import normal_chat, e2ee_chat
from modules.cookie_utils import load_cookies

console = Console()

def show_logo():
    with open("assets/saiim_logo.txt", "r", encoding="utf-8") as f:
        logo = f.read()
    console.print(Panel.fit(logo, title="[bold green]SAIIM MESSENGER", border_style="bold blue"))

def show_menu():
    console.print("\n[bold cyan][1][/bold cyan] Normal Chat Conversation")
    console.print("[bold cyan][2][/bold cyan] End-to-End Encrypted (E2EE) Conversation")
    choice = console.input("\n[bold yellow]Choose Option [1/2]: [/bold yellow]")
    return choice.strip()

def check_cookie():
    try:
        cookies = load_cookies()
        response = requests.get("https://www.facebook.com/me", cookies=cookies)
        if "name" in response.text.lower() or "/me/picture" in response.text.lower():
            # Extract username from the title
            name = response.text.split("<title>")[1].split("</title>")[0]
            console.print(f"[bold green]✅ Cookie Valid! Logged in as:[/bold green] [yellow]{name}[/yellow]")
            return True
        else:
            console.print("[red]❌ Cookie invalid or expired! Please update your cookies.txt[/red]")
            return False
    except Exception as e:
        console.print(f"[red]Error checking cookie:[/red] {e}")
        return False

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
