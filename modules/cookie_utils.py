# modules/cookie_utils.py

def load_cookies():
    cookies = []
    try:
        with open("cookies.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line and "c_user=" in line and "xs=" in line:
                    cookies.append(line)
    except FileNotFoundError:
        pass
    return cookies
