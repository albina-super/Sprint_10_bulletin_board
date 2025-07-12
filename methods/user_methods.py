from json import loads

import requests
from allure import step

from data import BASE_URL, REGISTER_USER_URL, LOGIN_USER_URL


class UserMethods:

    @step('Регистрируем юзера')
    def register_user(self, params):
        response = requests.post(f'{BASE_URL}{REGISTER_USER_URL}', json=params)
        return response.status_code, loads(response.text)


    @step('Логин пользвателя')
    def login_user(self, params):
        response = requests.post(f'{BASE_URL}{LOGIN_USER_URL}', json=params)
        return response.status_code, loads(response.text)