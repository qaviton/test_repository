from tests.pages.components.page import Page
from tests.parameters.locators import locator
from tests.pages.components.login import Login


class HomePage(Page):
    def __init__(self, driver, *args, **kwargs):
        Page.__init__(self, driver, *args, **kwargs)
        self.login = Login()

    def qaviton_menu_home_button(self):
        return self.find(locator.go_to_login)

    def navigate_to_Login(self, weight=10, *args, **kwargs):
        self.qaviton_menu_home_button().click()
        self.wait_until_page_loads()
