import pytest
import requests
from helpers import PersonData
from urls import URL, Endpoints


@pytest.fixture
def create_user():
    payload = PersonData.create_correct_user_data()
    response = requests.post(URL.main_url + Endpoints.CREATE_USER, data=payload)
    yield payload, response
    token = response.json().get('accessToken')
    if token:
        requests.delete(URL.main_url + Endpoints.DELETE_USER, headers={"Authorization": token})
