import allure
import requests
from helpers import PersonData
from urls import URL, Endpoints
from data import StatusCode


class TestLoginUser:
    @allure.title('Регистрация существующего пользователя')
    def test_user_login(self, create_user):
        response = create_user
        login = requests.post(URL.main_url + Endpoints.LOGIN, data=response[0])
        assert login.status_code == StatusCode.OK
        assert login.json().get("success") is True

    @allure.title('Регистрация несуществующего пользователя')
    def test_login_nonexistent_user(self):
        login_request = requests.post(URL.main_url + Endpoints.LOGIN,
                                      data=PersonData.create_incorrect_user_data_without_name())
        assert login_request.status_code == StatusCode.UNAUTHORIZED
        assert login_request.json().get("success") is False
