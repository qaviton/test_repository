from qaviton.page import Page as page
from functional_web_tests.tests.config.locators import locator


class SignUp(page):
    """signup component"""
    def signup_user(self):
        return self.find(locator.signup_user)

    def signup_pass(self):
        return self.find(locator.signup_pass)

    def signup_with_mail_button(self):
        return self.find(locator.signup_with_mail_button)

    def __call__(self, username, password):
        self.signup_user().send(username)
        self.signup_pass().send(password)
        self.click(('class', 'signup-form__terms-checkbox'))
        self.click(('class', 'button'))
        self.wait_until_page_loads()
        self.confirm_element_is_deleted(locator.signup_with_mail_button)

    def sign_up_with_mail_no_robot(self, username, password):
        self.signup_with_mail_button().click()
        self.signup_user().send(username)
        self.signup_pass().send(password)
        self.click(('class', 'signup-form__terms-checkbox'))
        self.click(('class', 'button'))
        self.wait_until_page_loads()
        self.confirm_element_is_deleted(locator.signup_with_mail_button)

    def sign_up_with_mail_and_robot(self, username, password):
        self.signup_with_mail_button().click()
        self.signup_user().send(username)
        self.signup_pass().send(password)
        self.click(('id', 'no_robot'))
        self.click(('class', 'signup-form__terms-checkbox'))
        self.click(('class', 'button'))
        self.wait_until_page_loads()
        self.confirm_element_is_deleted(locator.signup_with_mail_button)

    def sign_up_with_robot(self, username, password):
        self.signup_with_mail_button().click()
        self.signup_user().send(username)
        self.signup_pass().send(password)
        self.click(('id', 'no_robot'))
        self.click(('class', 'signup-form__terms-checkbox'))
        self.click(('class', 'button'))
        self.wait_until_page_loads()
        self.confirm_element_is_deleted(locator.signup_with_mail_button)

    def sign_up_no_terms(self, username, password):
        self.signup_user().send(username)
        self.signup_pass().send(password)
        self.click(('class', 'button'))
        self.wait_until_page_loads()
        self.confirm_element_is_deleted(locator.signup_with_mail_button)

    def sign_up_with_mail_no_terms(self, username, password):
        self.signup_with_mail_button().click()
        self.signup_user().send(username)
        self.signup_pass().send(password)
        self.click(('class', 'button'))
        self.wait_until_page_loads()
        self.confirm_element_is_deleted(locator.signup_with_mail_button)

    def sign_up_with_mail_and_robot_no_terms(self, username, password):
        self.signup_with_mail_button().click()
        self.signup_user().send(username)
        self.signup_pass().send(password)
        self.click(('id', 'no_robot'))
        self.click(('class', 'button'))
        self.wait_until_page_loads()
        self.confirm_element_is_deleted(locator.signup_with_mail_button)

    def sign_up_with_robot_and_mail_no_terms(self, username, password):
        self.signup_user().send(username)
        self.signup_pass().send(password)
        self.click(('id', 'no_robot'))
        self.click(('class', 'button'))
        self.wait_until_page_loads()
        self.confirm_element_is_deleted(locator.signup_with_mail_button)

