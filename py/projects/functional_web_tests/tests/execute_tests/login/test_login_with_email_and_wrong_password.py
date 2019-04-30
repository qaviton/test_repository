def test_login_mail_invalid_password(app):
    app.navigate(app.home.login)
    app.home.login.with_error(
        username="idanhakimi@gmail.com",
        password="ida$",
        error="invalid character")


def test_login_mail_wrong_password(app):
    app.navigate(app.home.login)
    app.home.login.with_error(
        username="idanhakimi@gmail.com",
        password="idan23",
        error="password not found")


def test_login_mail_invalid_password_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(
        username="idanhakimi@gmail.com",
        password="ida$",
        error="invalid character")


def test_login_mail_wrong_password_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(
        username="idanhakimi@gmail.com",
        password="idan23",
        error="password not found")




