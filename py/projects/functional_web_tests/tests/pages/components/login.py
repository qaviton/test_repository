import time
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

    def login_instagram(self):
        return self.find(locator.login_instagram)

    def login_linkedin(self):
        return self.find(locator.login_linkedin)

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


    def with_facebook(self, username, password):
        number_of_handles = len(self.driver.window_handles)
        self.login_facebook().click()
        self.wait_until_page_loads()

        t = time.time()
        while number_of_handles == len(self.driver.window_handles):
            time.sleep(0.005)
            if number_of_handles < len(self.driver.window_handles):
                break
            elif time.time() - t >= 5:
                raise Exception('facebook login window failed to open')

        main_window = self.driver.current_window_handle
        facebook_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(facebook_window)

        self.wait_until_page_loads()
        self.find(('id', 'email')).send(username)
        self.find(('id', 'pass')).send(password)
        self.find(('id', 'loginbutton')).click()
        self.wait_until_page_loads()
        self.confirm_element_is_deleted(('id', 'loginbutton'))
        facebook_permission_confirmation = self.try_to_find_all(('type', 'submit'))
        if len(facebook_permission_confirmation) == 4:
            facebook_permission_confirmation[-2].click()
            self.wait_until_page_loads()
            self.confirm_element_is_deleted(('element', facebook_permission_confirmation[-2]))
        self.driver.close()
        # switch back
        self.driver.switch_to.window(main_window)
        self.wait_until_page_loads()
        self.confirm_element_is_deleted(locator.login_facebook)


    def with_error_facebook(self, username, password):
        number_of_handles = len(self.driver.window_handles)
        self.login_facebook().click()
        self.wait_until_page_loads()

        t = time.time()
        while number_of_handles == len(self.driver.window_handles):
            time.sleep(0.005)
            if number_of_handles < len(self.driver.window_handles):
                break
            elif time.time() - t >= 5:
                raise Exception('facebook login window failed to open')

        main_window = self.driver.current_window_handle
        facebook_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(facebook_window)

        self.wait_until_page_loads()
        self.find(('id', 'email')).send(username)
        self.find(('id', 'pass')).send(password)
        self.find(('id', 'loginbutton')).click()
        self.wait_until_page_loads()
        try:
            self.find(('data-testid', 'undefined'))
        except Exception as e:
            raise Exception('facebook login error message was expected but found none: {}'.format(e))



    # def with_instagram(self):
    #     self.login_instagram().click()
    #     self.wait_until_page_loads()
    #     self.confirm_element_is_deleted(locator.login_instagram)
    #
    # def with_instagram_error(self, error):
    #     self.login_instagram().click()
    #     self.wait_until_page_loads()
    #     self.find(locator.text(error))
    #
    # def with_linkedin(self):
    #     self.login_linkedin().click()
    #     self.wait_until_page_loads()
    #     self.confirm_element_is_deleted(locator.login_linkedin)
    #
    # def with_linkedin_error(self, error):
    #     self.login_linkedin().click()
    #     self.wait_until_page_loads()
    #     self.find(locator.text(error))