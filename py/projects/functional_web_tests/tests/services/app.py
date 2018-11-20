from qaviton.navigator import Navigator
from tests.parameters.locators import locator
from tests.pages.components.page import Page
from tests.pages.qaviton_home import QavitonHomePage


class App(Page):
    """use the app page to include all your
    pages/components/api/services/flows
    in a single page application
    """

    locator = locator

    def __init__(self, driver, platform):
        Page.__init__(self, driver, platform=platform)
        self.qaviton_home = QavitonHomePage(driver)

        self.navigate = Navigator(self.qaviton_home, auto_connect=self)
