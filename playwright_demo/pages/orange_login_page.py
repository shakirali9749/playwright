from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def navigate(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", timeout=60000)

    def login(self, username: str, password: str):
        print("Filling username...")
        # breakpoint()
        self.username_input.fill(username)
        print("Filling password...")
        self.password_input.fill(password)
        print("Clicking login...")
        self.login_button.click()

        # Wait for dashboard to appear
        # self.page.wait_for_url("**/dashboard/**", timeout=10000)
        print("Login completed.")
        # self.page.screenshot(path="login_result.png")
