from qaviton.locator import Locator


class locator(Locator):
    type_submit = ('type', 'submit')
    logo = ('id', 'site-logo')
    go_to_login = ('xpath', '/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
    login_user = ('id', 'login_field')
    login_pass = ('id', 'password')
    login_email = ('id', 'login_field')
    login_button = ('type', 'submit')



#class locator(Locator):
    #type_submit = ('type', 'submit')
    #logo = ('id', 'site-logo')
    #go_to_login = ('id', 'login')
    #login_user = ('id', 'login_user')
    #login_email = ('id', 'login_email')
    #login_pass = ('id', 'login_pass')
    #login_button = ('id', 'login_button')