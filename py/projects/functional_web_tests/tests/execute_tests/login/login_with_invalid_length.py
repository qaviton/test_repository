def login_invalid_username_length_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="i", password="1qugiufg", error="invalid username length")


def login_invalid_password_length_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idan", password="idanhakimi1233444idanhsdsdsdsdsdakimi", error="invalid password length")


def login_invalid_email_length_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="ida1292hakimiidanhakimi234@gmail.com", password="idan", error="invalid email length")

def login_invalid_username_length_test_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(username="i", password="1qugiufg", error="invalid username length")

def login_invalid_password_length_test_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(username="idan", password="idanhakimi1233444idanhsdsdsdsdsdakimi",
                                  error="invalid password length")

def login_invalid_email_length_test_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(username="ida1292hakimiidanhakimi234@gmail.com", password="idan",
                                  error="invalid email length")


