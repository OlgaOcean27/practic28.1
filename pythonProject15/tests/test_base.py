from api.client import order_base_client
from resources.prepare_data import Networks, getIDsFromResponse
from serializers.orders import User
import requests

token = str

#      пинг-тест

def test_ping():
    response = order_base_client.booking_ping()
    assert response.status_code == 201
    if response.status_code == 201:
        print('SUCCESS: Ping test - PASSED')

#       тест создания токена

def test_token():
    token = order_base_client.create_token()
    assert token.status_code == 200
    if token.status_code == 200:
        print('SUCCESS: Token is GOTTEN')

#       тест  получение всех ID c построчным выводом результата для визуализации

def testGetAllIDs():
    try:
        r = requests.get(Networks.Booking)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    response = r.json()
    ids = getIDsFromResponse(response)
    print(*ids, sep="\n")

#       тест получение списка из 0 пользователей

def test_users_get_no_users():
    response = []
    users = [User(**user) for user in response]
    assert len(users) == 0

#     тест получение рандомного пользователя

def test_users_get_one_user():
    response = [{"id": 123, "first_name": "John", "last_name": "Doe"}]
    users = [User(**user) for user in response]
    assert len(users) == 1
    assert users[0].id == 123
    assert users[0].first_name == "John"
    assert users[0].last_name == "Doe"

#     тест получение максимального количества пользователей
def test_users_get_max_users():
    response = [{"id": i, "first_name": "User", "last_name": str(i)} for i in range(1000)]
    users = [User(**user) for user in response]
    assert len(users) == 1000
    assert users[-1].id == 999
    assert users[-1].first_name == "User"
    assert users[-1].last_name == "999"

#      тест поиск мин кол-ва пользователей:

def test_users_get_min_users():
    response = [{"id": i, "first_name": "User", "last_name": str(i)} for i in range(1)]
    users = [User(**user) for user in response]
    assert len(users) == 1

#      тест поиска максимального кол-ва пользователей по определенному имени

def test_users_get_specific_users():
    response = [{"id": i, "first_name": "Leon", "last_name": str(i)} for i in range(1000)]
    users = [User(**user) for user in response]
    assert len(users) == 1000
    assert users[0].first_name == "Leon"
    assert users[0].last_name == "1000"

