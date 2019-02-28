##sign up after try sign in with few entries
def test_signup_with_mail_no_robot_no_navbar(app):
    app.navigate(app.home.signup)
    app.home.signup.sign_up_with_mail_no_robot(username="sdsdsdsd@gmail.com", password="sdsdsdtterssd1239")

def test_signup_with_mail_and_robot_no_navbar(app):
    app.navigate(app.home.signup)
    app.home.signup.sign_up_with_mail_and_robot(username="sdsdsdsd@gmail.com", password="sdsdsdtterssd1239")

def test_signup_with_mail_no_robot_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.signup)
    app.home.signup.sign_up_with_mail_no_robot(username="sdsdsdsd@gmail.com", password="sdsdsdtterssd1239")

def test_signup_with_mail_and_robot_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.signup)
    app.home.signup.sign_up_with_mail_and_robot(username="sdsdsdsd@gmail.com", password="sdsdsdtterssd1239")


##regular signup
def test_regular_signup_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.signup)
    app.home.signup(username="sdsdsdsd@gmail.com", password="sdsdsdtterssd1239")

def test_regular_signup_no_navbar(app):
    app.navigate(app.home.signup)
    app.home.signup(username="sdsdsdsd@gmail.com", password="sdsdsdtterssd1239")

##regular signup with robot

def test_regular_signup_with_robot_and_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home.signup)
    app.home.signup.sign_up_with_robot(username="sdsdsdsd@gmail.com", password="sdsdsdtterssd1239")

def test_regular_signup_with_robot_no_navbar(app):
    app.navigate(app.home.signup)
    app.home.signup.sign_up_with_robot(username="sdsdsdsd@gmail.com", password="sdsdsdtterssd1239")