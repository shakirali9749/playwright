import re
from playwright.sync_api import Page
from pages.orange_login_page import LoginPage
from pages.orange_home_page import HomePage

def test_logout(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)

    # Navigate to the login page
    login_page.navigate()

    # Perform login
    login_page.login("Admin", "admin123")

    home_page.logout()






"""
if you need your test in single file, then you can use the following code snippet:
def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", timeout=60000)
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("listitem").filter(has_text="Amruta Patil").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()
"""