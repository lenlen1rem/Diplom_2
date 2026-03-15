import requests
from curl import URL
import allure


class AddOrder:
    @staticmethod
    @allure.step("Создание заказа")
    def add_order(order_data: dict, headers=None):
        if headers is None:
            headers = {}
        return requests.post(URL.ADD_ORDER, json=order_data, headers=headers)
    