def test_login_with_linkedin(app):
    app.navigate(app.home.login)
    app.home.login.with_linkedin(
        username="isdsdi@gmail.com",
        password="1sdsd")


def test_login_with_linkedin_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_linkedin(
        username="isdsdi@gmail.com",
        password="1sdsd")
