def test_login_with_facebook(app):
    app.navigate(app.home.login)
    app.home.login.with_facebook(
        username="idanhakimi@gmail.com",
        password="1qaz@WSX")

# def test_login_with_facebook_failure(app):
#         app.navigate(app.home.login)
#         app.home.login.with_error_facebook(username="idanhakimi@gmail.com", password="1qaz@WSX")


def test_login_with_facebook_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_facebook(
        username="idanhakimi@gmail.com",
        password="1qaz@WSX")
