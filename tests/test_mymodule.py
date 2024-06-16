from unittest.mock import Mock, patch

from src.my_module import fetch_data
from src.utils import get_transaction_amount


# Тестовая функция
def test_fetch_data():
    # Создаем Mock объект для имитации клиента API
    mock_api_client = Mock()

    # Настраиваем Mock, чтобы он возвращал объект с нужными атрибутами
    mock_api_client.get.return_value.status_code = 200
    mock_api_client.get.return_value.json.return_value = {"key": "value"}

    # Вызываем функцию с Mock объектом
    result = fetch_data(mock_api_client, "http://fakeurl.com")

    # Проверяем, что результат верный
    assert result == {"key": "value"}

    # Проверяем, что метод get был вызван с правильным URL
    mock_api_client.get.assert_called_with("http://fakeurl.com")


# Тестовая функция
def test_fetch_data_200():
    # Создаем Mock объект для имитации клиента API
    mock_api_client = Mock()

    # Настраиваем Mock, чтобы он возвращал объект с нужными атрибутами
    mock_api_client.get.return_value.status_code = 404
    mock_api_client.get.return_value.json.return_value = None

    # Вызываем функцию с Mock объектом
    result = fetch_data(mock_api_client, "http://fakeurl.com")

    # Проверяем, что результат верный
    assert result == None

    # Проверяем, что метод get был вызван с правильным URL
    mock_api_client.get.assert_called_with("http://fakeurl.com")


# Допустим, что нам нужно замокать следующую функцию execute():
#
#
# result = get_drive_service().files().insert(body='body', convert=True).execute()
#
#
# Для этого нужно пропатчить все функции, которые предшествуют вызову функции execute():
#
#
# from mock import patch
#
# with patch('path.to.import.get_drive_service') as service_mock:
#
#    service_mock.return_value.files.return_value.insert.\
#
#    return_value.execute.return_value = {'key': 'value', 'status': 200}

# def test_get_transaction_amount():
#     with patch('path.to.import.get_transaction_amount') as service_mock:
