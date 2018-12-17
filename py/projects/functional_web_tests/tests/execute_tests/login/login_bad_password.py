def login_invalid_user_character_test(app):
    app.navigate(app.home.login)
    app.home.login.error(usename="idan", password="id$n", error="invalid character")


def login_invalid_password_test(app):
    app.navigate(app.home.login)
    app.home.login.error(usename="idan", password="idan11229922", error="password not found")


#done