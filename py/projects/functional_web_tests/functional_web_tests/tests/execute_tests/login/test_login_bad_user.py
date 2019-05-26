def test_login_invalid_user_character(app):
    app.navigate(app.home.login)
    app.home.login.with_error(
        username="id$a",
        password="1qugiufg",
        error="invalid character")


def test_login_invalid_user(app):
    app.navigate(app.home.login)
    app.home.login.with_error(
        username="ida129299",
        password="1tgjoj",
        error="user not found")


def test_login_invalid_user_character_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(
        username="id$a",
        password="1qugiufg",
        error="invalid character")


def test_login_invalid_user_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(
        username="ida129299",
        password="1tgjoj",
        error="user not found")
