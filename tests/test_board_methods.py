import pytest
import allure
from data import CATEGORIES, DATA_FOR_POST, CREATED_STATUS, SUCCESS_STATUS, UPDATE_POST_DATA
from methods.board_methods import BoardMethods


class TestBoardMethods:


    @pytest.mark.parametrize('types', CATEGORIES)
    def test_create_board_with_all_types(self,  types, user):
        allure.dynamic.title('Проверка создания объявление с разными категорями')
        board = BoardMethods()
        DATA_FOR_POST['category'] = types
        status, response = board.create_post(DATA_FOR_POST, user)
        assert status == CREATED_STATUS
        assert status == CREATED_STATUS and response is not None

    @allure.title('Проверка удаления объявления')
    def test_delete_post(self, post, user):
        board = BoardMethods()
        status, response = board.delete_post(board_id=post, token=user)
        assert status == SUCCESS_STATUS and response == {
            "message": "Объявление удалено успешно"
        }

    @allure.title('Проверка обновления объявления')
    def test_update_post_success(self, post, user):
        board = BoardMethods()
        code, response = board.update_board(UPDATE_POST_DATA, user, post)
        assert code == SUCCESS_STATUS and response is not None

    @allure.title('Проверка обновления объявления под другим пользователем')
    def test_update_from_other_user(self, post, user_2):
        board = BoardMethods()
        code, response = board.update_board(UPDATE_POST_DATA, user_2, post)
        assert code == 401 and response == {'message': 'Оффер не найден или у вас нет прав на его редактирование', 'error': 'Unauthorized', 'statusCode': 401}
