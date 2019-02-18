def login_invalid_pass_character_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idantheking", password="id$n", error="invalid character")
