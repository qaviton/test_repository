def test_login_email(app):
    app.navigate(app.home.login)
    app.home.login(
        username="idanha@net4uc.com",
        password="1qaz@WSXqwerASDF")


def test_login_email_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login(
        username="idanha@net4uc.com",
        password="1qaz@WSXqwerASDF")
