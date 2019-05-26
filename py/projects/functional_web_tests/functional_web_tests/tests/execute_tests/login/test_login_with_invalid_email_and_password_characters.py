def test_login_invalid_email_pass_character(app):
    app.navigate(app.home.login)
    app.home.login.with_error(
        username="ida1292#gmail.com",
        password="id#@Aan",
        error="invalid characters for both mail and password")


def test_login_invalid_email_pass_character_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(
        username="ida1292#gmail.com",
        password="id#@Aan",
        error="invalid characters for both mail and password")
