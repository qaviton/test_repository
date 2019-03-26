def login_invalid_pass_character_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idantheking", password="id$n", error="invalid character")

def login_invalid_pass_character_test_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(username="idantheking", password="id$n", error="invalid character")

