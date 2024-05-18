import pytest, requests


from ..utils.base_url import dev_url_base
from .payloads.createRegisterPayload import payload_to_create_register

BASE_URL = f"{dev_url_base}"


def test_create_register_with_success():
    resource = "/create-register"
    url = BASE_URL + resource
    body = payload_to_create_register
    response = requests.post(
        url,
        json=body
    )
    message_that_should_come_in_the_response = "Register created with success!"
    data = response.json()
    assert response.status_code == 201
    assert data["message"] == should_message_to_response
