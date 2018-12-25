def login_invalid_email_character_test(app):
    app.navigate(app.home.login)
    app.home.login.error(email="ida1292#gmail.com", password="idan", error="invalid character")


#Done