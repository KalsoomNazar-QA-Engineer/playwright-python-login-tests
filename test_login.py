from playwright.sync_api import Page
from pages.login_page import LoginPage


def test_valid_login(page: Page):
    """TC_001: Valid login with correct credentials"""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("student", "Password123")
    login_page.expect_success()


def test_invalid_username(page: Page):
    """TC_002: Invalid username with valid password"""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("incorrectUser", "Password123")
    login_page.expect_error("Your username is invalid!")


def test_invalid_password(page: Page):
    """TC_003: Valid username with invalid password"""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("student", "incorrectPassword")
    login_page.expect_error("Your password is invalid!")


def test_empty_username(page: Page):
    """TC_004: Username empty"""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("", "Password123")
    login_page.expect_error("Your username is invalid!")


def test_empty_password(page: Page):
    """TC_005: Password empty"""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("student", "")
    login_page.expect_error("Your password is invalid!")


def test_both_fields_empty(page: Page):
    """TC_006: Both fields empty"""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("", "")
    login_page.expect_error("Your username is invalid!")