from data import CREATED_STATUS, MY_USER_DATA, BAD_REQUEST_STATUS
from helpers import data_for_user
from methods.user_methods import UserMethods
import allure

class TestUserMethods:

    @allure.title('проверка успешной регистрации')
    def test_user_register_success(self):
        user = UserMethods()
        data = data_for_user()
        status, response = user.register_user(data)
        assert status == CREATED_STATUS and 'access_token' in response


    @allure.title('проверка одинаковых пользователей')
    def test_same_user_register(self):
        user = UserMethods()
        status, response = user.register_user(MY_USER_DATA)
        assert status == BAD_REQUEST_STATUS and response['message'] == 'Почта уже используется'


    @allure.title('проверка успешного логина')
    def test_user_login_success(self):
        user = UserMethods()
        status, response = user.login_user(MY_USER_DATA)
        assert status == CREATED_STATUS and 'access_token' in response['token']