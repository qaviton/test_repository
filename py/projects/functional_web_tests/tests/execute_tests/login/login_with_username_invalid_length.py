def login_invalid_user_length_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="i", password="1qugiufg", error="invalid username length")

def login_invalid_user_length_test_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(username="i", password="1qugiufg", error="invalid username length")



