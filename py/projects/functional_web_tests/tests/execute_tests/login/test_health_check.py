def test_health_check(app):
    app.navigate(app.home)


def test_navbar_health_check(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home)
