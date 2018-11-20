def test_login(app):
    app.navigate(app.qaviton_home.login)
    app.qaviton_home.login(usename="ida", password="idan")
