import pytest, requests
from pytest import fixture

from ..utils.base_url import dev_url_base
from .payloads.createRegisterPayload import payload_to_create_register

BASE_URL = f"{dev_url_base}"


@pytest.fixture
def create_register_to_delete():
    resource = "/create-register"
    url = BASE_URL + resource
    body = payload_to_create_register
    response = requests.post(
        url,
        json=body
    )
    data = response.json()
    return data["id"]


def test_create_register_with_success(create_register_to_delete):
    resource = "/delete-register/"
    id_to_delete = create_register_to_delete
    id_register_to_delete = str(id_to_delete)
    url = BASE_URL + resource + id_register_to_delete

    response = requests.delete(
        url
    )

    message_that_should_come_in_the_response = "Register deleted with success"
    data = response.json()

    assert response.status_code == 200
    assert data["message"] == message_that_should_come_in_the_response
