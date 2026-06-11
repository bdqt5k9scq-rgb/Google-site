"""Capture screenshots of the UN SDGs website for PPT embedding."""
import os
from playwright.sync_api import sync_playwright

PAGES = [
    ("home", "http://localhost:5173/"),
    ("sdgs", "http://localhost:5173/sdgs"),
    ("carbon", "http://localhost:5173/carbon-footprint"),
    ("actnow", "http://localhost:5173/act-now"),
]

OUTPUT_DIR = "output/screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900})

    for name, url in PAGES:
        print(f"Capturing: {name} ({url})")
        page.goto(url, wait_until="networkidle", timeout=15000)
        page.wait_for_timeout(1000)  # let GSAP animations settle
        path = os.path.join(OUTPUT_DIR, f"{name}.png")
        page.screenshot(path=path, full_page=False)
        print(f"  Saved: {path}")

    browser.close()
    print("Done — 4 screenshots captured.")
