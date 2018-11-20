from qaviton.locator import Locator


class locator(Locator):

    # you can use a variety of methods to build locators
    type_submit = ('type', 'submit')
    qaviton_logo = ('id', 'site-logo')
    qaviton_menu_home_button = ('xpath', '//a[text()="LOGIN"]')
    SIGN_UP_FOR_A_BETA = ('text', 'SIGN UP FOR A BETA')
    opl_user_login = ('id', 'opl_user_login')
    opl_user_pass = ('id', 'opl_user_pass')
    login_button = ('id', 'login_button')

    # you can use the Locator directly to build your locator
    qaviton_email_demo_request = Locator.xpath('//input[@placeholder="Your Email"]')
    qaviton_company_demo_request = Locator.xpath('//input[@placeholder="Company"]')
    qaviton_name_demo_request = Locator.xpath('//input[@placeholder="Name"]')

    qaviton_send_demo_request = Locator.tuple(
        Locator.xpath('//button[@type="submit"]//*[text()="SEND"]'),
        Locator.index(type_submit, index=0))