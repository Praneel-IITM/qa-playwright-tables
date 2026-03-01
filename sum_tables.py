from playwright.sync_api import sync_playwright
import re

total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for seed in range(34, 44):
        url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
        page.goto(url)
        page.wait_for_selector("table")

        tables = page.locator("table").all_inner_texts()

        for table in tables:
            numbers = re.findall(r"-?\d+", table)
            total_sum += sum(map(int, numbers))

    browser.close()

print("TOTAL SUM:", total_sum)
