from qaviton.navigator import Navigator
from functional_web_tests.tests.config.locators import locator
from functional_web_tests.tests.pages.components.page import Page
from functional_web_tests.tests.pages.home import HomePage


class App(Page):
    """use the app page to include all your
    pages/components/api/services/flows
    in a single page application
    """

    locator = locator

    def __init__(self, driver, platform):
        Page.__init__(self, driver, platform=platform)
        self.home = HomePage(driver)

        self.navigate = Navigator(self.home, auto_connect=self)
