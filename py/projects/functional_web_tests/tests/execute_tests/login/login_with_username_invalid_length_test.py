def test_login_invalid_user_length(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="i", password="1qugiufg", error="invalid username length")