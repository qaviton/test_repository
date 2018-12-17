from tests.pages.components.page import Page
from tests.config.locators import locator
from tests.pages.components.login import Login


class HomePage(Page):
    def __init__(self, driver):
        Page.__init__(self, driver)
        self.login = Login(driver)

    def go_to_login(self):
        return self.find(locator.go_to_login)

    def navigate_to_Login(self, weight=10, *args, **kwargs):
        self.go_to_login().click()
        self.wait_until_page_loads()
