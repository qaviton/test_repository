def login_invalid_email_pass_character_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="ida1292#gmail.com", password="id#@Aan", error="invalid characters for both mail and password")

def login_invalid_email_pass_character_test_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(username="ida1292#gmail.com", password="id#@Aan",
                                  error="invalid characters for both mail and password")

