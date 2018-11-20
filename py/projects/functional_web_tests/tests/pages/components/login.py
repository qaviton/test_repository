from qaviton.page import Page as page
from tests.parameters.locators import locator


class Login(page):
    """login component"""
    def opl_user_login(self):
        return self.find(locator.opl_user_login)

    def opl_user_pass(self):
        return self.find(locator.opl_user_pass)

    def login_button(self):
        return self.find(locator.login_button)

    def __call__(self, username, password):
        self.opl_user_login().send(username)
        self.opl_user_pass().send(password)
        self.login_button().click()
        self.wait_until_page_loads()
        self.confirm_element_is_deleted(locator.opl_user_login)