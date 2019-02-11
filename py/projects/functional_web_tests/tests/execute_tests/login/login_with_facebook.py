# def test_login_with_facebook(app):
#     app.navigate(app.home.login)
#     app.home.login.with_facebook(username="idanhsdsdsdsd@gmail.com", password="asdasdsad")

def test_login_with_facebook_failure(app):
        app.navigate(app.home.login)
        app.home.login.with_error_facebook(username="idanhsdsdsdsd@gmail.com", password="asdasdsad")

