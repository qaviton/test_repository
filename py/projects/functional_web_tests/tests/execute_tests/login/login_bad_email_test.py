def test_login_email_invalid_character(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="ida1292#gmail.com", password="1qaz@WSXqwerASDF", error="invalid character")


def test_login_email_invalid(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idannnn@gmail.com", password="1qaz@WSXqwerASDF", error="email not found")

