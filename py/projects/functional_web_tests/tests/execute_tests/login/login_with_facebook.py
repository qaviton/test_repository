def test_login_with_facebook(app):
    app.navigate(app.home.login)
    app.home.login.with_facebook()

def test_login_with_bad_facebook(app):
        app.navigate(app.home.login)
        app.home.login.with_error_facebook(error="facebook not found")
