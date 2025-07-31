# modules/logger.py

from rich.console import Console
from datetime import datetime

console = Console()

def log_info(msg, type="info"):
    color = {
        "info": "cyan",
        "success": "green",
        "error": "red",
        "warn": "yellow"
    }.get(type, "white")
    
    time_str = datetime.now().strftime("%H:%M:%S")
    console.print(f"[{color}][{time_str}][/][bold {color}] {msg}[/bold {color}]")
