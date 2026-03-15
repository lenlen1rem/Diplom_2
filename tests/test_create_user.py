import pytest
import allure
import requests
from helpers import PersonData
from urls import URL, Endpoints
from data import StatusCode, TextResponse

class TestCreateUser:
    @allure.title('Тест на создание пользователя')
    def test_create_user(self, create_user):
        response = create_user
        assert response[1].json().get("success") is True
        assert response[1].status_code == StatusCode.OK
