import requests
from modules.utils import load_messages, load_thread, simulate_typing, delay

def send_normal_messages():
    cookie = input("Enter your Facebook cookie: ")
    messages = load_messages("messages.txt")
    thread_id = load_thread("thread.txt")

    headers = {
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0',
    }

    for msg in messages:
        simulate_typing(msg)
        # Dummy simulation, you must replace this with Graph API or real endpoint
        print(f"Sending to thread {thread_id}: {msg}")
        delay()
        except Exception as e:
            print(f"❌ Error: {e}")

        index += 1
        time.sleep(60)  # 🕒 Change delay here (default: 60 seconds)
