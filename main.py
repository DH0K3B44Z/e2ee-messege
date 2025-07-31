# main.py

import os
from rich.console import Console
from rich.panel import Panel
from modules import normal_chat, e2ee_chat

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

def main():
    os.system("clear" if os.name == "posix" else "cls")
    show_logo()
    choice = show_menu()

    if choice == '1':
        normal_chat.start()
    elif choice == '2':
        e2ee_chat.start()
    else:
        console.print("[red]Invalid option! Exiting.[/red]")

if __name__ == "__main__":
    main()
def print_logo():
    with open("assets/saiim_logo.txt", "r") as f:
        from rich import print
        print(f"[bold green]{f.read()}[/bold green]")
