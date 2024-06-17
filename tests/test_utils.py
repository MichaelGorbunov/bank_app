import json
# import random
from unittest.mock import patch

from src.utils import get_transaction_amount, get_transaction_from_file

# import pytest
# import requests


def test_get_transaction_amount():
    """вывод суммы транзакции"""
    test_dict = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.59", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert get_transaction_amount(test_dict) == 31957.59


def test_get_transaction_amount_no_amount():
    """в транзакции нет суммы"""
    test_dict = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert get_transaction_amount(test_dict) == 0.0


def test_get_transaction_amount_no_transact():
    """пустая транзакция"""
    assert get_transaction_amount("") == 0.0


def test_get_transaction_amount_usd():
    """проверка конвертации"""
    test_dict = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert get_transaction_amount(test_dict) != 1


@patch("builtins.open")
@patch("os.path.exists")
def test_get_transaction_from_file(mock_exists, mock_open):
    """чтение виртуального файла"""
    # Mock os.path.exists to return True
    mock_exists.return_value = True

    # Mock open function to return a JSON string
    mock_open.return_value.__enter__.return_value.read.return_value = '[{"id": 207126257, "state": "EXECUTED"}]'

    file_path = "..\\data\\operations.json"
    transactions = get_transaction_from_file(file_path)

    assert transactions == [{"id": 207126257, "state": "EXECUTED"}]
    # mock_exists.assert_called_once_with(file_path)
    # mock_open.assert_called_once_with(file_path, 'r', encoding='utf-8')


def test_get_transaction_from_file_no_json():
    """чтение ошибочного файла"""
    assert get_transaction_from_file("..\\data\\myfile.txt") == []


@patch("builtins.open", create=True)
def test_get_transactions_from_file_patch(mock_open):
    """тесты с виртуальным файлом"""

    mock_file = mock_open.return_value.__enter__.return_value

    # в файле список словарей
    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert get_transaction_from_file("test.json") == [{"test": "test"}]

    # "пустой файл"
    mock_file.read.return_value = ""
    assert get_transaction_from_file("test.json") == []


# def test_get_transaction_from_file_no_json_exept():
#     with pytest. as err:
#         get_transaction_from_file('..\data\\myfile.txt')
#
#     # # Проверяем, что сообщение об ошибке соответствует ожидаемому
#    assert err == "***"
# @patch("builtins.open")
# @patch("os.path.exists")
# def test_get_transaction_from_file_not_a_list(mock_exists, mock_open):
#     """файл не json"""
#     mock_exists.return_value = True
#     mock_open.return_value.__enter__.return_value.read.return_value = "{}"
#
#     # file_path = 'data/operations.json'
#     file_path = "myfile.txt"
#     transactions = get_transaction_from_file(file_path)
#
#     assert transactions == {}
#     # mock_exists.assert_called_once_with(file_path)
#     mock_open.assert_called_once_with(file_path, "r", encoding="utf-8")
#
#
# @patch("builtins.open")
# @patch("os.path.exists")
# def test_data_transactions_json_decode_error(mock_open):
#     """Функция проверяет, что функция возвращает False, если файл содержит невалидный JSON"""
#     # создаем mock для файла
#     mock_file = mock_open(read_data='invalid json')
#     mock_file.return_value.__iter__.return_value = ['invalid json']  # <--- Add this line
#
#     # патчим функцию open
#     with patch('builtins.open', mock_file):
#         # вызываем функцию data_transactions
#         transactions_dict = get_transaction_from_file('myfile.txt')
#
#         # проверяем результат
#         self.assertEqual(transactions_dict, [])
