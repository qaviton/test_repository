from tests.pages.components.page import Page
from tests.config.locators import locator
from tests.pages.components.login import Login
from tests.pages.components.signup import SignUp
from tests.pages.components.home_navbar import HomeNavBar
from tests.config import url


class HomePage(Page):
    def __init__(self, driver):
        Page.__init__(self, driver)
        self.login = Login(driver)
        self.signup = SignUp(driver)
        self.navbar = HomeNavBar(driver)

    def go_to_login(self):
        return self.find(locator.go_to_login)

    def go_to_sign_up(self):
        return self.find(locator.go_to_sign_up)

    def go_to_home_navbar(self):
        return self.find(locator.go_to_home_navbar)

    def navigate_to_Login(self, weight=10, *args, **kwargs):
        #self.get_page(url.home)
        self.go_to_login().click()
        self.wait_until_page_loads()

    def navigate_to_SignUp(self, weight=10, *args, **kwargs):
        self.go_to_sign_up().click()
        self.wait_until_page_loads()

    def navigate_to_HomeNavBar(self, weight=10, *args, **kwargs):
        self.go_to_home_navbar().click()
        self.wait_until_page_loads()
