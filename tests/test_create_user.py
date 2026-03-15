import pytest
from helper import GenerateRandom
from api_methods.create_user_method import AddUser
import allure


DUPLICATE_LOGIN_MSG = "User already exists"
MISSING_DATA_MSG = "Email, password and name are required fields"

class TestAddUser:

    @allure.title("Тест на регистрацию пользователя")
    def test_add_user(self, delete_user_after_test):
        user_data = GenerateRandom.generate_user_body()
        response = AddUser.register_new_user(user_data=user_data)
        response_join = response.json()

        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert response.json()["success"] == True
        assert "accessToken" in response.json()
        
        delete_user_after_test(response_join["accessToken"])


    @allure.title("Тест на невозможность создать двух одинаковых пользователей")
    def test_cannot_add_user(self, user_for_create):
        duplicate_data = {
        "email": user_for_create["email"],
        "password": user_for_create["password"],
        "name": user_for_create["name"]
        }
        second_response = AddUser.register_new_user(user_data = duplicate_data)

        assert second_response.status_code == 403, f"Ожидался код 403, но получен {second_response.status_code}"
        assert second_response.json()["message"] == DUPLICATE_LOGIN_MSG, f"Ожидался ответ {DUPLICATE_LOGIN_MSG}, но получен {second_response.json()}"

    @allure.title("Тест на возврат ошибки при отсутствии одного из полей при создании пользователя")
    @pytest.mark.parametrize("remote_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, remote_field):
        user_data = GenerateRandom.generate_user_body()
        user_data.pop(remote_field)   
        response = AddUser.register_new_user(user_data=user_data)

        assert response.status_code == 403, f"Ожидался код 403, но получен {response.status_code}"
        assert response.json()["message"] == MISSING_DATA_MSG, f"Ожидался ответ {MISSING_DATA_MSG}, но получен {response.json()}"