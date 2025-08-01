"""
youtube: https://www.youtube.com/watch?v=VZ5LU8vHT0s&list=PLhW3qG5bs-L8WcAa9cfXaqGe0-Cq85y4X&index=2

"""

import pytest
from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        with p.chromium.launch(headless=True) as browser:
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://google.com")
            return page.title()


if __name__ == "__main__":
    main()
