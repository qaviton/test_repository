from qaviton.page import Page as page
from functional_web_tests.tests.config import url


class Page(page):
    """component with common behavior to all pages & components alike.
    all of your pages & components should inherit from this common page.

    you should always include here a navigation to your initial login page(starting point)
    so that dependent tests could always start fresh if needed.
    """

    def navigate_to_HomePage(self, weight=3, *args, **kwargs):
        self.driver.get(url.home)
        self.wait_until_page_loads()

