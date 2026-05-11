from playwright.sync_api import sync_playwright

url = "https://realpython.github.io/fake-jobs/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url, timeout=30000)
    page.wait_for_timeout(3000)  # let JS load
    html = page.content()
    browser.close()

with open("file_1.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done!")