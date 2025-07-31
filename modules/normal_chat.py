# modules/normal_chat.py

from modules.sender_core import send_message
from rich.console import Console

console = Console()

def start():
    thread_id = input("Enter Normal Chat Thread ID: ").strip()
    try:
        with open("messages/normal.txt", "r", encoding="utf-8") as f:
            messages = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        console.print("[red]messages/normal.txt not found![/red]")
        return

    console.print("[green]Starting normal chat messaging...[/green]")

    while True:
        for msg in messages:
            ok = send_message(thread_id, msg, typing=True)
            if ok:
                console.print(f"[bold cyan]Sent:[/bold cyan] {msg}")
            else:
                console.print(f"[bold red]Failed:[/bold red] {msg}")
            time.sleep(60)
