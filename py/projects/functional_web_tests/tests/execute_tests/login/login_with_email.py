def test_login_email(app):
    app.navigate(app.home.login)
    app.home.login(username="idanha@net4uc.com", password="1qaz@WSXqwerASDF")
