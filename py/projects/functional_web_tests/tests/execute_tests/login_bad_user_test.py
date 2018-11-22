def login_invalid_user_character_test(app):
    app.navigate(app.qaviton_home.login)
    app.qaviton_home.login.error(usename="id$a", password="idan", error="invalid character")


def login_invalid_user_test(app):
    app.navigate(app.qaviton_home.login)
    app.qaviton_home.login.error(usename="ida12999", password="idan", error="user not found")
