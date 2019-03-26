def login_empty_username_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="", password="idan", error="missing username")


def login_empty_email_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="", password="idan", error="missing email")


def login_username_empty_password_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idan", password="", error="missing password")


def login_email_empty_password_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idanhakimi@gmail.com", password="", error="missing password")

def login_empty_username_test_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(username="", password="idan", error="missing username")

def login_empty_email_test_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(username="", password="idan", error="missing email")

def login_username_empty_password_test_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(username="idan", password="", error="missing password")

def login_email_empty_password_test_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(username="idanhakimi@gmail.com", password="", error="missing password")

