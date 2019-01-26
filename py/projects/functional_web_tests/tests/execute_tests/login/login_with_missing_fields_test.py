def test_login_empty_username(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="", password="idan", error="missing username")

def test_login_empty_email(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="", password="idan", error="missing email")


def test_login_username_empty_password(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idan", password="", error="missing password"

def test_login_email_empty_password(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idanmi@gmail.com", password="", error="missing password")