from qaviton.page import Page as page
from tests.config.locators import locator


class Login(page):
    """login component"""
    def login_user(self):
        return self.find(locator.login_user)

    def login_pass(self):
        return self.find(locator.login_pass)

    def login_button(self):
        return self.find(locator.login_button)

    def login_facebook(self):
        return self.find(locator.login_facebook)

    def __call__(self, username, password):
        self.login_user().send(username)
        self.login_pass().send(password)
        self.login_button().click()
        self.wait_until_page_loads()
        self.confirm_element_is_deleted(locator.login_user)

    def with_error(self, username, password, error):
        self.login_user().send(username)
        self.login_pass().send(password)
        self.login_button().click()
        self.wait_until_page_loads()
        self.find(locator.text(error))
        #self.confirm_element_is_deleted(locator.login_user)

    def with_facebook(self):
        self.login_facebook().click()
        self.wait_until_page_loads()
        self.confirm_element_is_deleted(locator.login_facebook)

    def with_error_facebook(self, error):
        self.login_facebook().click()
        self.wait_until_page_loads()
        self.find(locator.text(error))
