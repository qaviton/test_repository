def login_invalid_user_character_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="id$a", password="1qugiufg", error="invalid character")


def login_invalid_user_test(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="ida129299", password="1tgjoj", error="user not found")



#done :)
