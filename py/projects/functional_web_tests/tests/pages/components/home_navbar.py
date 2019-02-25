import time
from qaviton.page import Page as page
from tests.config.locators import locator


class HomeNavBar(page):
    """navbar component"""
    def go_to_sign_up(self):
        return self.find(locator.go_to_sign_up)

    def go_to_login(self):
        return self.find(locator.go_to_login)

    def navigate_to_Login(self, weight=10, *args, **kwargs):
        self.go_to_login().click()
        self.wait_until_page_loads()

    def navigate_to_SignUp(self, weight=10, *args, **kwargs):
        self.go_to_sign_up().click()
        self.wait_until_page_loads()