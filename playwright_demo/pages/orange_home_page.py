from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.profile_dropdown = page.get_by_role("banner").get_by_role("img", name="profile picture")
        self.logout_button = page.get_by_role("menuitem", name="Logout")

    def logout(self):
        # Wait for profile dropdown to be visible or attached
        expect(self.profile_dropdown).to_be_visible(timeout=10000)
        self.profile_dropdown.click()

        # Wait for logout button before clicking
        expect(self.logout_button).to_be_visible(timeout=5000)
        self.logout_button.click()
