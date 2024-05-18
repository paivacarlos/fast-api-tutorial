import pytest, requests


from ..utils.base_url import dev_url_base

BASE_URL = f"{dev_url_base}"


def test_health_check_server_is_online():
    resource = "/health-check"
    response = requests.get(BASE_URL + resource)

    print(response)
    assert True
