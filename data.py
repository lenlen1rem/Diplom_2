#тестовые данные пользователей
class TestUser:
    email = 'test_api_user_1@example.com'
    password = 'Password123!'
    name = 'TestUser'

#невалидные данные для тестов
class InvalidData:
    #для регистрации
    invalid_users = [
        {"email": "", "password": "password123", "name": "Test"},
        {"email": "invalid_email", "password": "password123", "name": "Test"},
        {"email": "test@example.com", "password": "", "name": "Test"},
        {"email": "test@example.com", "password": "123", "name": ""},
    ]
    
    #для авторизации
    wrong_credentials = [
        {"email": "wrong@example.com", "password": "wrongpassword"},
        {"email": "test_api_user_1@example.com", "password": "wrongpassword"},
    ]
    
    #невалидные хеши ингредиентов
    invalid_hashes = ['invalid_hash_1', 'invalid_hash_2']

#ожидаемые ответы
class ExpectedResponses:
    success_true = {'success': True}
    user_exists = {'success': False, 'message': 'User already exists'}
    missing_fields = {'success': False, 'message': 'Email, password and name are required fields'}
    invalid_creds = {'success': False, 'message': 'email or password are incorrect'}
    unauthorized = {'success': False, 'message': 'You should be authorized'}
    no_ingredients = {'success': False, 'message': 'Ingredient ids must be provided'}