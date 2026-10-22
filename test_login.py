from playwright.sync_api import Page, expect

URL = "https://practicetestautomation.com/practice-test-login/"


def test_valid_login(page: Page):
    """TC_001: Valid login with correct credentials"""
    page.goto(URL)
    page.fill("#username", "student")
    page.fill("#password", "Password123")
    page.click("#submit")
    expect(page.locator("h1")).to_have_text("Logged In Successfully")


def test_invalid_username(page: Page):
    """TC_002: Invalid username with valid password"""
    page.goto(URL)
    page.fill("#username", "incorrectUser")
    page.fill("#password", "Password123")
    page.click("#submit")
    expect(page.locator("#error")).to_have_text("Your username is invalid!")


def test_invalid_password(page: Page):
    """TC_003: Valid username with invalid password"""
    page.goto(URL)
    page.fill("#username", "student")
    page.fill("#password", "incorrectPassword")
    page.click("#submit")
    expect(page.locator("#error")).to_have_text("Your password is invalid!")


def test_empty_username(page: Page):
    """TC_004: Username empty"""
    page.goto(URL)
    page.fill("#password", "Password123")
    page.click("#submit")
    expect(page.locator("#error")).to_have_text("Your username is invalid!")


def test_empty_password(page: Page):
    """TC_005: Password empty"""
    page.goto(URL)
    page.fill("#username", "student")
    page.click("#submit")
    expect(page.locator("#error")).to_have_text("Your password is invalid!")


def test_both_fields_empty(page: Page):
    """TC_006: Both fields empty"""
    page.goto(URL)
    page.click("#submit")
    expect(page.locator("#error")).to_have_text("Your username is invalid!")