def test_login_with_github(app):
    app.navigate(app.home.login)
    app.home.login.with_github(username="idsdsdsdmi", password="Isdsdsdsdhj")


