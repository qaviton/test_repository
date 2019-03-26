def test_login_with_signout(app):
    app.navigate(app.home.login)
    app.home.login.sign_out(username="ifgdgh@gmail.com", password="1rtyrtyyry")

def test_login_with_signout_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.login)
    app.home.login.sign_out(username="ifgdgh@gmail.com", password="1rtyrtyyry")


