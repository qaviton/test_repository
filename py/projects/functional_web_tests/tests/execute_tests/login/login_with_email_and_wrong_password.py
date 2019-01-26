def login_mail_invalid_password__test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idanhakimi@gmail.com", password="ida$", error="invalid character")


def login_mail_wrong_password__test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idanhakimi@gmail.com", password="idan23", error="password not found")



#Done :)

