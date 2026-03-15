import requests
from curl import URL
import allure


class AddUser:
    @staticmethod
    @allure.step("Создание пользователя")
    def register_new_user(user_data: dict):
        return requests.post(URL.ADD_USER, json=user_data)