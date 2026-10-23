from playwright.sync_api import Page, expect


class LoginPage:
    URL = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.submit_button = page.locator("#submit")
        self.error_message = page.locator("#error")
        self.success_heading = page.locator("h1")

    def open(self):
        self.page.goto(self.URL, timeout=60000, wait_until="domcontentloaded")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def expect_error(self, message: str):
        expect(self.error_message).to_have_text(message)

    def expect_success(self):
        expect(self.success_heading).to_have_text("Logged In Successfully")