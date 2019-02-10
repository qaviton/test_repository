def test_login_with_instagram(app):
    app.navigate(app.home.login)
    app.home.login.with_instagram()

def test_login_with_instagram_failure(app):
        app.navigate(app.home.login)
        app.home.login.with_error_instagram(error="instagram not found")