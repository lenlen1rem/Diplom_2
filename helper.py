import requests
import random
import string
from curl import URL
from faker import Faker
import uuid


class GenerateRandom:
    @staticmethod
    def generate_user_body():
        
        faker = Faker()
        unique_id = str(uuid.uuid4())[:8]
        return {
            "email": f"{faker.user_name()}_{unique_id}@test.com",
            "password": faker.password(),
            "name": faker.first_name()
        }


    @staticmethod
    def register_new_user_and_return_login_password():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login_pass = []
        
        email = generate_random_string(20)
        password = generate_random_string(10)
        name = generate_random_string(10)

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(URL.ADD_USER, json=payload)

        if response.status_code == 200:
            login_pass.append(email)
            login_pass.append(password)

        return login_pass
    
    @staticmethod
    def generate_invalid_hash(length=24):
        
        chars = string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for _ in range(length))