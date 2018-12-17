def test_login_email(app):
    app.navigate(app.home.login)
    app.home.login(email="idanhakimi@gmail.com", password="idan")


#done