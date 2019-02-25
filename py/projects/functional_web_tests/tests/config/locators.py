from qaviton.locator import Locator


# class locator(Locator):
#     type_submit = ('type', 'submit')
#     logo = ('id', 'site-logo')
#     go_to_login = ('id', 'login')
#     login_user = ('id', 'login_user')
#     login_pass = ('id', 'login_pass')
#     login_facebook = ('id', 'login_facebook')
#    login_instagram = ('id', 'login_instagram')
#    login_linkedin = ('id', 'login_linkedin')
#     login_button = ('id', 'login_button')



class locator(Locator):
    type_submit = ('type', 'submit')
    logo = ('id', 'site-logo')
    go_to_login = ('id', 'idcta-link')
    login_user = ('id', 'signup-form__email')
    login_pass = ('id', 'password-input__password')
    login_facebook = ('class', 'facebook')
    login_google = ('text', 'Sign in with Google')
    login_github = ('text', 'Sign in with GitHub')
    login_twitter = ('text', 'Sign in with Twitter')
    login_linkedin = ('key', 'linkedin')
    login_email = ('id', 'login_field')
    go_to_sign_out = ('id', 'idcta-link')
    go_to_sign_up = ('id', 'go_to_signup')
    go_to_home_navbar = ('id', 'navigation__navbar')
    signup_with_mail_button = ('id', 'mail_button')
    signup_user = ('id', 'signup-form__email')
    signup_pass = ('id', 'password-input__password')
    login_button = ('id', 'submit-button')

