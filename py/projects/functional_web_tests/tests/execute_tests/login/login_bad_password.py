def login_invalid_password_character_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idantheking", password="id$n", error="invalid character")


def login_invalid_password_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idantheking", password="idan11229922", error="password not found")

def login_invalid_password_character_test_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(username="idantheking", password="id$n", error="invalid character")

def login_invalid_password_test_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(username="idantheking", password="idan11229922", error="password not found")


