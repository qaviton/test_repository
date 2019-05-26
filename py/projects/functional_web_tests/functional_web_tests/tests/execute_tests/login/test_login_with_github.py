def test_login_with_github(app):
    app.navigate(app.home.login)
    app.home.login.with_github(
        username="idsdsdsdmi",
        password="Isdsdsdsdhj")


def test_login_with_github_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_github(
        username="idsdsdsdmi",
        password="Isdsdsdsdhj")
