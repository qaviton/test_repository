from tests.pages.components.page import Page
from tests.parameters.locators import locator
from tests.pages.components.login import Login


class QavitonHomePage(Page):
    def __init__(self, driver, *args, **kwargs):
        Page.__init__(self, driver, *args, **kwargs)
        self.login = Login()

    def SIGN_UP_FOR_A_BETA(self):
        return self.find(locator.SIGN_UP_FOR_A_BETA)

    def qaviton_menu_home_button(self):
        return self.find(locator.qaviton_menu_home_button)

    def qaviton_logo(self):
        return self.find(locator.qaviton_logo)

    def qaviton_send_demo_request(self):
        return self.find(locator.qaviton_send_demo_request)

    def qaviton_name_demo_request(self):
        return self.find(locator.qaviton_name_demo_request)

    def qaviton_company_demo_request(self):
        return self.find(locator.qaviton_company_demo_request)

    def qaviton_email_demo_request(self):
        return self.find(locator.qaviton_email_demo_request)

    def navigate_to_Login(self, weight=10, *args, **kwargs):
        self.qaviton_menu_home_button().click()
        self.wait_until_page_loads()