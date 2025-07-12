from json import loads

import requests
from allure import step

from data import BASE_URL, CREATE_POST, UPDATE_POST, POSTS


class BoardMethods:


    @step('создаем ордер')
    def create_post(self, params, token):
        headers = {
            'Authorization': f'Bearer {token}'
        }

        form_data = [(key, (None, str(value))) for key, value in params.items()]

        response = requests.post(
            f'{BASE_URL}{CREATE_POST}',
            files=form_data,
            headers=headers,
            timeout=30
        )

        return response.status_code, loads(response.text)


    @step('Обновляем данные')
    def update_board(self, params, token, id):
        response = requests.patch(f'{BASE_URL}{UPDATE_POST}/{id}', json=params, headers={'Authorization': f'Bearer {token}'})
        return response.status_code, loads(response.text)


    @step('удаляем объявление')
    def delete_post(self, board_id, token):
        response = requests.delete(f'{BASE_URL}{POSTS}/{board_id}', headers={'Authorization': f'Bearer {token}'})
        return response.status_code, loads(response.text)