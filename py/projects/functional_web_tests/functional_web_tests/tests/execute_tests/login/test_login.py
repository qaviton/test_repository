def test_login(app):
    app.navigate(app.home.login)
    app.home.login(
        username="idantheking",
        password="1qaz@WSXqwerASDF")


def test_login_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login(
        username="idantheking",
        password="1qaz@WSXqwerASDF")
