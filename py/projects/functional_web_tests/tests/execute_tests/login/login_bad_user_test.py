def login_invalid_user_character_test(app):
    app.navigate(app.home.login)
    app.home.login.error(usename="id$a", password="idan", error="invalid character")


def login_invalid_user_test(app):
    app.navigate(app.home.login)
    app.home.login.error(usename="ida129299", password="idan", error="user not found")
