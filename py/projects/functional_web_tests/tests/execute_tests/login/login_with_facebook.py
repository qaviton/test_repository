def test_login_with_facebook(app):
    app.navigate(app.home.login)
    app.home.login(usename="idan", password="idan")



##How to do that