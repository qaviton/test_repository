def test_login_with_google(app):
    app.navigate(app.home.login)
    app.home.login.with_google(username="idsdsda@digithouse.net", password="1sdsdsdsdsdsd")



# def with_google_new_tab(app):
#     app.navigate(app.home.login)
#     app.home.login.with_google(username="idanha@digithouse.net", password="15935755")


# def test_login_with_google_failure(app):
#         app.navigate(app.home.login)
#         app.home.login.with_error_google(username="idanhsdsdsdsd@gmail.com", password="asdasdsad")

