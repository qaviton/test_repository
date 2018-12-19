def login_invalid_user_length_test(app):
    app.navigate(app.home.login)
    app.home.login.error(usename="id$a3983kkkk3kkkkk", password="idan", error="username is too long")


def login_invalid_password_length_test(app):
    app.navigate(app.home.login)
    app.home.login.error(usename="idan", password="idanhakimi1233444idanhakimi", error="password is too long")

def login_invalid_email_length_test(app):
    app.navigate(app.home.login)
    app.home.login.error(email="ida1292hakimiidanhakimi234@gmail.com", password="idan", error="email is too long")



#Done