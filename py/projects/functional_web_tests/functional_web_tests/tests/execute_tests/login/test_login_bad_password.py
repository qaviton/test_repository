def test_login_invalid_password_character(app):
    app.navigate(app.home.login)
    app.home.login.with_error(
        username="idantheking",
        password="id$n",
        error="invalid character")


def test_login_invalid_password(app):
    app.navigate(app.home.login)
    app.home.login.with_error(
        username="idantheking",
        password="idan11229922",
        error="password not found")


def test_login_invalid_password_character_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(
        username="idantheking",
        password="id$n",
        error="invalid character")


def test_login_invalid_password_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(
        username="idantheking",
        password="idan11229922",
        error="password not found")
