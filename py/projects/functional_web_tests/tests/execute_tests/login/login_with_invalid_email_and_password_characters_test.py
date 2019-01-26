def test_login_invalid_email_password_character(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="ida1292#gmail.com", password="id#@Aan", error="invalid email and password")

