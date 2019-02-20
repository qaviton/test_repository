def test_login_with_twitter(app):
    app.navigate(app.home.login)
    app.home.login.with_twitter(username="idasdsdsd@gmail.com", password="15sdsdsd5")