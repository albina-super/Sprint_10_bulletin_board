import random
import string


def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(['example.com', 'testmail.com', 'mail.io'])
    return f"{username}@{domain}"


def data_for_user():
    return {
        "email": generate_random_email(),
        "password": "TestPass123!",
        "submitPassword": "TestPass123!"
    }
