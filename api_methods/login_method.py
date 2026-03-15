import requests
from curl import URL
import allure


class LoginUser:
    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(user_login: dict):
        return requests.post(URL.LOGIN_USER, json=user_login)