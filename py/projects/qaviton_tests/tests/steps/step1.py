import os
from sys import path


def login(username, password):
    """
    :step: login
    :param username:
    :param password:
    :return token:
    :call: app.login
    """
    if os.name == 'net':
        print(1)

    elif os.name == 'linux':
        print(2)
    else:
        print('macOS')

    return os.name


def logout():
    """
    :step: log out
    :from tests.steps.step1 import logout
    :call: app.login
    """
    if os.name == 'net':
        print(1)

    elif os.name == 'linux':
        print(2)
    else:
        print('macOS')


def go_to_cart():
    """
    :step:
    :import web.go_to_cart
    :call: web.go_to_cart
    """
    if os.name == 'net':
        print(1)

    elif os.name == 'linux':
        print(2)
    else:
        print('macOS')


def checkout():
    """
    :step:
    """
    if os.name == 'net':
        print(1)

    elif os.name == 'linux':
        print(2)
    else:
        print('macOS')
