def test_login_with_twitter(app):
    app.navigate(app.home.login)
    app.home.login.with_twitter(
        username="idasdsdsd@gmail.com",
        password="15sdsdsd5")


def test_login_with_twitter_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_twitter(
        username="idasdsdsd@gmail.com",
        password="15sdsdsd5")
