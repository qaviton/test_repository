def test_login_email(app):
    app.navigate(app.home.login)
    app.home.login(username="idan@gmail.com", password="1sswerASDF")


