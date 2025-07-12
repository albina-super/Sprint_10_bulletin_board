import pytest

from data import MY_USER_DATA, DATA_FOR_POST_2, MY_USER_DATA_2
from methods.board_methods import BoardMethods
from methods.user_methods import UserMethods


@pytest.fixture
def user():
    user = UserMethods()
    code, response = user.login_user(MY_USER_DATA)
    return response['token']['access_token']


@pytest.fixture
def user_2():
    user = UserMethods()
    code, response = user.login_user(MY_USER_DATA_2)
    return response['token']['access_token']


@pytest.fixture
def post():
    post = BoardMethods()
    code, user_data =  UserMethods().login_user(MY_USER_DATA)
    code_post, response = post.create_post(DATA_FOR_POST_2, user_data['token']['access_token'])
    return response['id']