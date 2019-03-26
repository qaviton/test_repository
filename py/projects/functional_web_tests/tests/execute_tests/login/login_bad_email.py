def login_invalid_email_character_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="ida1292#gmail.com", password="1qaz@WSXqwerASDF", error="invalid character")


def login_invalid_email_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idannnn@gmail.com", password="1qaz@WSXqwerASDF", error="email not found")


def login_invalid_email_character_test_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(username="ida1292#gmail.com", password="1qaz@WSXqwerASDF", error="invalid character")


def login_invalid_email_test_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.with_error(username="idannnn@gmail.com", password="1qaz@WSXqwerASDF", error="email not found")

