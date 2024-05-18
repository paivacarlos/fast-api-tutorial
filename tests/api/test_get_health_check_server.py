import pytest, requests


from ..utils.base_url import dev_url_base

BASE_URL = f"{dev_url_base}"


def test_health_check_server_is_online():
    resource = "/health-check"
    response = requests.get(BASE_URL + resource)

    data = response.json()
    message_that_should_come_in_the_response = "We are online! ;)"

    assert response.status_code == 200
    assert data["message"] == messagem_that_should_come_in_the_response
