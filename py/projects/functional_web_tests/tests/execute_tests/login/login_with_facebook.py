def test_login(app):
    app.navigate(app.home.login)
    app.home.login(usename="idan", password="idan")



