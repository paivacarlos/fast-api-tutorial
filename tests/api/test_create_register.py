import pytest, requests, copy


from ..utils.base_url import dev_url_base
from .payloads.createRegisterPayload import payload_to_create_register

BASE_URL = f"{dev_url_base}"
CPF_INVALID = "01625708051"


def test_create_register_with_success():
    resource = "/create-register"
    url = BASE_URL + resource
    body = copy.deepcopy(payload_to_create_register)
    response = requests.post(
        url,
        json=body
    )
    message_that_should_come_in_the_response = "Register created with success!"
    data = response.json()
    assert response.status_code == 201
    assert data["message"] == message_that_should_come_in_the_response


def test_create_register_cpf_invalid():
    resource = "/create-register"
    url = BASE_URL + resource
    body = copy.deepcopy(payload_to_create_register)
    body["cpf"] = CPF_INVALID
    response = requests.post(
        url,
        json=body
    )
    message_that_should_come_in_the_response = "Invalid CPF"
    data = response.json()
    assert response.status_code == 400
    assert data["detail"] == message_that_should_come_in_the_response
