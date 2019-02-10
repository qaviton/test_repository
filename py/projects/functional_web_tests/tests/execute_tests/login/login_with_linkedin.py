def test_login_with_linkedin(app):
    app.navigate(app.home.login)
    app.home.login.with_linkedin()

def test_login_with_linkedin_failure(app):
        app.navigate(app.home.login)
        app.home.login.with_error_linkedin(error="linkedin not found")