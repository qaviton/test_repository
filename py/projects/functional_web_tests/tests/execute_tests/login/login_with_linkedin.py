def test_login_with_linkedin(app):
    app.navigate(app.home.login)
    app.home.login.with_linkedin(username="isdsdi@gmail.com", password="1sdsd")