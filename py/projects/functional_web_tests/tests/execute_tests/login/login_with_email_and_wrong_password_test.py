def test_login_email_invalid_password(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idanmi@gmail.com", password="ida$", error="invalid password")


def test_login_email_wrong_password(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idani@gmail.com", password="idan23", error="password not found")

