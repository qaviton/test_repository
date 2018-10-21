import requests


def test_sanity():
    """assert request is valid"""
    assert requests.get("https://www.qaviton.com/").status_code == 200