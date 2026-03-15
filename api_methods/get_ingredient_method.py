import requests
from curl import URL
import allure


class GetIngredient:
    @staticmethod
    @allure.step("Получение списка ингредиентов")
    def get_ingredient():
        return requests.get(URL.DATA_INGREDIENT)