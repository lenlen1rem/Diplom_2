import pytest
import allure
import requests
from helpers import PersonData
from urls import URL, Endpoints
from data import StatusCode, TextResponse

class TestCreateUser:
    @allure.title('Unique user creation test')
    def test_create_user(self, create_user):
        response = create_user
        assert response[1].json().get("success") is True
        assert response[1].status_code == StatusCode.OK
