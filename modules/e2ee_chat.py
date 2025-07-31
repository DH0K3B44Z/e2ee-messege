import asyncio
from playwright.async_api import async_playwright
from modules.utils import load_messages, load_thread, delay

async def send_messages(playwright, cookie, thread_id, messages):
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    await page.goto("https://www.facebook.com")
    await context.add_cookies([{
        'name': pair.split("=")[0].strip(),
        'value': pair.split("=")[1].strip(),
        'domain': '.facebook.com',
        'path': '/',
        'httpOnly': True,
        'secure': True
    } for pair in cookie.split(";")])

    await page.goto(f"https://www.facebook.com/messages/e2ee/t/{thread_id}")
    await page.wait_for_selector('[contenteditable="true"]')

    for msg in messages:
        await page.type('[contenteditable="true"]', msg, delay=100)
        await page.keyboard.press("Enter")
        print(f"Sent: {msg}")
        await asyncio.sleep(55)

    await browser.close()

def send_e2ee_messages():
    cookie = input("Enter your Facebook cookie: ")
    messages = load_messages("messages.txt")
    thread_id = load_thread("thread.txt")
    asyncio.run(run(cookie, thread_id, messages))

async def run(cookie, thread_id, messages):
    async with async_playwright() as p:
        await send_messages(p, cookie, thread_id, messages)
