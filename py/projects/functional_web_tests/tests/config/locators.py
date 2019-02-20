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
    go_to_login = ('text', ' Log In ')
    login_user = ('id', 'login_field')
    login_pass = ('id', 'password')
    login_facebook = ('class', 'facebook')
    login_google = ('text', 'Sign in with Google')
    login_github = ('text', 'Sign in with GitHub')
    login_twitter = ('text', 'Sign in with Twitter')
    login_linkedin = ('key', 'linkedin')
    login_email = ('id', 'login_field')
    login_button = ('type', 'submit')

