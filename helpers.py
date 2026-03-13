#вспомогательные функции для тестов


from generators import generate_email, generate_password, generate_name


def generate_user_data():
    """генерация данных нового пользователя"""
    return {
        'email': generate_email(),
        'password': generate_password(),
        'name': generate_name()
    }