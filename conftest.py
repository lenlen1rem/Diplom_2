import pytest
import random
from helper import GenerateRandom
from api_methods.create_user_method import AddUser
from api_methods.login_method import LoginUser
from api_methods.delete_user_method import DeleteUser
from api_methods.get_ingredient_method import GetIngredient
from helper import GenerateRandom


'''фикстура регистрации и авторизации пользователя'''
@pytest.fixture
def user_for_create():
    
    user_data = GenerateRandom.generate_user_body()
    response = AddUser.register_new_user(user_data=user_data)
    auth_response = LoginUser.login_user({
        "email": user_data["email"],
        "password": user_data["password"]
    })
    
    response_json = response.json()

    yield {
        "email": user_data["email"],
        "password": user_data["password"],
        "name": user_data["name"],
        "accessToken": response_json["accessToken"],
        "refreshToken": response_json["refreshToken"]
    }

    DeleteUser.delete_user(response_json["accessToken"])


'''фикстура для заказов'''
@pytest.fixture
def order_for_create():

    ingredients_response = GetIngredient.get_ingredient()
    ingredients_data = ingredients_response.json()
    
    all_ingredients = ingredients_data["data"]
    selected_ingredients = random.sample(all_ingredients, 3)
    
    ingredient_ids = []
    for ing in selected_ingredients:
        ingredient_ids.append(ing["_id"])
    
    return ingredient_ids

'''фикстура для удаления пользователя'''
@pytest.fixture
def delete_user_after_test():
    tokens = []
    
    def _add_token(access_token):
        tokens.append(access_token)
        return access_token
    
    yield _add_token

    for token in tokens:
        DeleteUser.delete_user(token)