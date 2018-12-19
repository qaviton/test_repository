def login_invalid_user_character_test(app):
    app.navigate(app.home.login)
    app.home.login.error(usename="id$a", password="idan", error="invalid character")



#Done