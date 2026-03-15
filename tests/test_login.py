import pytest
from api_methods.login_method import LoginUser
import allure


class TestLoginUser:
    
    @allure.title("Тест. Успешная авторизация пользователя")
    def test_login_user(self, user_for_create):
  
        login_data = {
            "email": user_for_create["email"],
            "password": user_for_create["password"]
        }

        response = LoginUser.login_user(login_data)
        
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
        assert response.json()["success"] == True
        assert "accessToken" in response.json()

    @allure.title("Тест. Авторизация с неверным эмеил или паролем")
    @pytest.mark.parametrize("invalid_field", ["email", "password"])
    def test_login_user_with_invalid_field(self, invalid_field, user_for_create):
        login_data = {
            "email": user_for_create["email"],
            "password": user_for_create["password"]
        }
        
        login_data[invalid_field] = 'change'
        response = LoginUser.login_user(login_data)

        assert response.status_code == 401, f"Ожидался код 401, но получен {response.status_code}"
        assert response.json()["success"] == False