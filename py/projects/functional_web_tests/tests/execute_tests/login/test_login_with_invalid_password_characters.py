def test_login_invalid_pass_character(app):
    app.navigate(app.home.login)
    app.home.login.with_error(
        username="idantheking",
        password="id$n",
        error="invalid character")


def test_login_invalid_pass_character_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(
        username="idantheking",
        password="id$n",
        error="invalid character")
