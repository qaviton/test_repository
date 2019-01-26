def test_login(app):
    app.navigate(app.home.login)
    app.home.login(username="idanidan", password="asd123")


