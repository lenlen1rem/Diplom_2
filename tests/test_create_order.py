import requests
import allure
from urls import URL, Endpoints
from data import StatusCode, TextResponse, Ingredients


class TestCreateOrder:
    @allure.title('Заказ авторизованным пользователем теста')
    def test_create_order_with_authorized_user(self, create_user):
        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        response = requests.post(URL.main_url + Endpoints.CREATE_ORDER, headers=headers, data=Ingredients.correct_ingredients_hash_data)
        assert response.status_code == StatusCode.OK
        assert response.json().get('success') is True

    @allure.title('Заказ неавторизованным пользователем теста')
    def test_create_order_by_unauthorized_user(self):
        response = requests.post(URL.main_url + Endpoints.CREATE_ORDER, data=Ingredients.correct_ingredients_hash_data)
        assert response.status_code == StatusCode.OK
        assert response.json().get('success') is True
