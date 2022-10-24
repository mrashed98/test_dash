import random
import string
import json


def generate_random_text(number_of_chars: int) -> str:
    return ''.join(random.choice(string.ascii_letters) for _ in range(number_of_chars))


def get_random_platform(platforms: list) -> str:
    return random.choice(platforms)


def get_creds():
    email = generate_random_text(7)+"@instabug.com"
    password = generate_random_text(12)
    data = {
        'email': email,
        'password': password
    }
    file = open('config/creds.json', 'w')
    json_object = json.dumps(data, indent=3)
    file.write(json_object)
    file.close()
    return email, password
