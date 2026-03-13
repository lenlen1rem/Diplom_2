class Endpoints:
    #базовый URL API
    base_url = 'https://stellarburgers.education-services.ru'
    
    #регистрация нового пользователя
    register = f'{base_url}/api/auth/register'
    #авторизация пользователя
    login = f'{base_url}/api/auth/login'
    #выход из системы
    logout = f'{base_url}/api/auth/logout'
    #обновление токена
    refresh_token = f'{base_url}/api/auth/token'
    #удаление пользователя
    user_delete = f'{base_url}/api/auth/user'
    #создание заказа
    create_order = f'{base_url}/api/orders'
    #получение заказов пользователя
    user_orders = f'{base_url}/api/orders'
    #получение ингредиентов
    ingredients = f'{base_url}/api/ingredients'