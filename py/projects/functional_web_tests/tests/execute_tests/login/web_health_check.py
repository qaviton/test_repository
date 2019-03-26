def health_check_test(app):
    app.navigate(app.home)

def health_check_test_with_navbar(app):
    app.navigate(app.home.navbar)
    app.navigate(app.home)

