import pytest
import requests


@pytest.mark.parametrize('n', range(100))
def test_normal_load(n):
    """run 100 requests in 40 sec"""
    assert requests.get("https://www.qaviton.com/").status_code == 200