import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import allure
import requests
import urls
from generators import generate_email, generate_password


class TestUserLogin:
    @allure.title('Вход под существующим пользователем')
    def test_login_success(self, new_user_data):
        """Вход с валидными учетными данными"""
        #регистрация
        register_response = requests.post(
            urls.Endpoints.register,  #используем register вместо REGISTER
            json=new_user_data
        )
        assert register_response.status_code == 200
        token = register_response.json()['accessToken']
        
        #вход
        payload = {
            'email': new_user_data['email'],
            'password': new_user_data['password']
        }
        response = requests.post(
            urls.Endpoints.login,  #используем login вместо LOGIN
            json=payload
        )
        
        assert response.status_code == 200
        assert response.json()['success'] is True
        
        #удаление пользователя
        headers = {'Authorization': f'Bearer {token}'}
        requests.delete(
            urls.Endpoints.user_delete,  #используем user_delete вместо USER
            headers=headers
        )

    @allure.title('Вход с неверными учетными данными')
    def test_login_invalid_credentials(self):
        """Вход с неверными учетными данными"""
        #тест 1: неверный email
        response = requests.post(urls.Endpoints.login, json={  #используем login
            'email': 'nonexistent@example.com',
            'password': 'password123'
        })
        assert response.status_code == 401
        assert response.json()['success'] is False
        
        #тест 2: неверный пароль
        response = requests.post(urls.Endpoints.login, json={  #используем login
            'email': 'test@example.com',
            'password': 'wrong_password'
        })
        assert response.status_code == 401
        assert response.json()['success'] is False