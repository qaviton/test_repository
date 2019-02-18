def test_login(app):
    app.navigate(app.home.login)
    app.home.login(username="idantheking", password="1qaz@WSXqwerASDF")
