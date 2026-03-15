import pytest
from helper import GenerateRandom
from api_methods.create_order_method import AddOrder
import allure


class TestAddOrder:
    
    @allure.title("Тест. Заказ авторизованным пользователем")
    def test_add_order_authorized_user(self, user_for_create, order_for_create):
           
        access_token = user_for_create["accessToken"]
        headers = {"Authorization": access_token}
        order_data = {"ingredients": order_for_create}
        
        order_response = AddOrder.add_order(order_data, headers=headers)
        order_json = order_response.json()

        assert order_response.status_code == 200, f"Ожидался код 200, но получен {order_response.status_code}"
        assert order_json["success"] == True
        assert order_json["order"]["number"] > 0

    @allure.title("Тест. Заказ неавторизованным пользователем")
    def test_add_order_unauthorized_user(self, order_for_create):
           
        order_data = {"ingredients": order_for_create}
        
        order_response = AddOrder.add_order(order_data)
        order_json = order_response.json()

        assert order_response.status_code == 401, f"Ожидался код 401, но получен {order_response.status_code}"
        assert order_json["success"] == False
    
    @allure.title("Тест. Заказ с ингредиентами")
    def test_add_order_with_ingredients(self, user_for_create, order_for_create):
           
        access_token = user_for_create["accessToken"]
        headers = {"Authorization": access_token}
        order_data = {"ingredients": order_for_create}
        
        order_response = AddOrder.add_order(order_data, headers=headers)
        order_json = order_response.json()

        assert order_response.status_code == 200, f"Ожидался код 200, но получен {order_response.status_code}"
        assert order_json["success"] == True
        assert "name" in order_json, f"Ожидалось имя бургера"
        assert order_json["order"]["number"] > 0

    @allure.title("Тест. Заказ без ингредиентов")
    def test_add_order_no_ingredients(self, user_for_create):
       
        access_token = user_for_create["accessToken"]
        headers = {"Authorization": access_token}
        order_data = {"ingredients": []}
        
        order_response = AddOrder.add_order(order_data, headers=headers)
        order_json = order_response.json()

        assert order_response.status_code == 400, f"Ожидался код 400, но получен {order_response.status_code}"
        assert order_json["success"] == False
        assert order_json["message"] == "Ingredient ids must be provided", f"Ожидалось сообщение об ошибке"


    @allure.title("Тест. Заказ с неверным хэшем ингредиентов")   
    def test_add_order_invalid_hash_ingrediens(self, user_for_create):
           
        access_token = user_for_create["accessToken"]
        headers = {"Authorization": access_token}

        invalid_hash_1 = GenerateRandom.generate_invalid_hash()
        invalid_hash_2 = GenerateRandom.generate_invalid_hash()
        order_data = {"ingredients": [invalid_hash_1, invalid_hash_2]}
        
        order_response = AddOrder.add_order(order_data, headers=headers)

        assert order_response.status_code == 500, f"Ожидался код 500, но получен {order_response.status_code}"