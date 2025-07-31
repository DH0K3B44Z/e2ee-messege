import json
from http.cookies import SimpleCookie
from requests import Session
from rich import print

def parse_cookie_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
        cookie = SimpleCookie()
        cookie.load(raw)
        return {key: morsel.value for key, morsel in cookie.items()}
    except Exception:
        return None

def check_and_print_username(cookie_path):
    cookies = parse_cookie_file(cookie_path)
    if not cookies:
        print("[red]❌ Cookie file invalid or missing![/red]")
        return False

    try:
        session = Session()
        session.cookies.update(cookies)
        r = session.get("https://m.facebook.com/me", allow_redirects=True)
        if "logout" in r.text and "name" in r.text:
            name = r.text.split('<title>')[1].split('</title>')[0]
            print(f"[green]✔ Cookie Valid! Logged in as:[/green] [bold]{name}[/bold]")
            return True
        else:
            print("[red]❌ Invalid or expired cookie![/red]")
            return False
    except Exception as e:
        print(f"[red]❌ Error checking cookie: {e}[/red]")
        return False
