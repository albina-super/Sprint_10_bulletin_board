BASE_URL = 'https://qa-desk.stand.praktikum-services.ru/api/'
REGISTER_USER_URL = 'signup'
LOGIN_USER_URL = 'signin'
CREATE_POST = 'create-listing/'
POSTS = 'listings'
UPDATE_POST = 'update-offer'


MY_USER_DATA = {
    "email": "user111@gmail.com",
    "password": "test123"
}


MY_USER_DATA_2 = {
    "email": "user424@test.com",
    "password": "test123"
}


CATEGORIES = [
    "Авто",
    "Книги",
    "Садоводство",
    "Хобби",
    "Технологии"
]


DATA_FOR_POST =  {
    "name": "Объявление",
    "condition": "Новый",
    "city": "Москва",
    "description": "новое объявление",
    "price": 230
}

DATA_FOR_POST_2 =  {
    "name": "Объявление 2",
    "condition": "Новый",
    "category": "Авто",
    "city": "Москва",
    "description": "новое объявление 2",
    "price": 23
}

UPDATE_POST_DATA = {
    "name": "табурет",
    "category": "Технологии",
    "condition": "Б/У",
    "city": "Новосибирск",
    "description": "новый товар",
    "price": 9090,
    "img1": None,
    "img2": None,
    "img3": None
}

CREATED_STATUS = 201
BAD_REQUEST_STATUS = 400
SUCCESS_STATUS = 200