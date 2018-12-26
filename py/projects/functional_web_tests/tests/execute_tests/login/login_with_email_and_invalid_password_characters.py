def login_invalid_email_pass_character_test(app):
    app.navigate(app.home.login)
    app.home.login.error(email="ida1292#gmail.com", password="id#@Aan", error="invalid characters for both mail and password")



#DONE