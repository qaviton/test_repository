def login_invalid_user_character_test(app):
    app.navigate(app.home.login)
    app.home.login.error(usename="idan", password="id$n", error="invalid character")


#Done