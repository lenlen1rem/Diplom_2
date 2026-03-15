class URL:
    BASE_URL = "https://stellarburgers.education-services.ru"

    ADD_USER = f"{BASE_URL}/api/auth/register"
    LOGIN_USER = f"{BASE_URL}/api/auth/login"
    DELETE_USER = f"{BASE_URL}/api/auth/user"

    ADD_ORDER = f"{BASE_URL}/api/orders"
    DATA_INGREDIENT = f"{BASE_URL}/api/ingredients"