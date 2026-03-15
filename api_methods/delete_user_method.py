import requests
from curl import URL
import allure


class DeleteUser:
    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(accessToken):
        headers = {"Authorization": accessToken}
        
        response = requests.delete(URL.DELETE_USER, headers=headers)
        return response