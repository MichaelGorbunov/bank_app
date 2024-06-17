import json
import os
# import random
# from unittest.mock import mock_open, patch
from unittest.mock import patch

import pytest

import src.utils
from config import DATA_DIR
from src.utils import get_transaction_amount, get_transaction_from_csv_file, get_transaction_from_file


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
    assert get_transaction_from_file(os.path.join(DATA_DIR, "myfile.txt")) == []


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


def test_get_transaction_from_csv_file_no_file():
    """файла нет"""
    # assert get_transaction_from_csv_file(os.path.join(DATA_DIR, "transactions1.csv")) == []
    with pytest.raises(FileNotFoundError) as excinfo:
        get_transaction_from_csv_file(os.path.join(DATA_DIR, "transactions1.csv"))
    assert str(excinfo.type.__name__) == "FileNotFoundError"


def test_get_transaction_from_file_no_file():
    """файла нет"""
    with pytest.raises(FileNotFoundError) as excinfo:
        get_transaction_from_file(os.path.join(DATA_DIR, "transactions1.json"))
    assert str(excinfo.type.__name__) == "FileNotFoundError"


DATA = """id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту
593027;CANCELED;2023-07-22T05:02:01Z;30368;Shilling;TZS;Visa 1959232722494097;Visa 6804119550473710;Перевод с карты на карту
"""


def test_get_transaction_from_csv_file():
    trans = get_transaction_from_csv_file(os.path.join(DATA_DIR, "test.csv"))
    assert trans == [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {"amount": "29740", "currency": {"name": "Peso", "code": "COP"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
        {
            "id": "593027",
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "operationAmount": {"amount": "30368", "currency": {"name": "Shilling", "code": "TZS"}},
            "description": "Перевод с карты на карту",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
        },
        {
            "id": "366176",
            "state": "EXECUTED",
            "date": "2020-08-02T09:35:18Z",
            "operationAmount": {"amount": "29482", "currency": {"name": "Rupiah", "code": "IDR"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 0325955596714937",
            "to": "Visa 3820488829287420",
        },
    ]


@patch('csv.reader')
def test_get_transaction_from_csv_file_mock(mock_reader):
    # Настраиваем mock_reader чтобы он возвращал нужный результат
    mock_reader.return_value = iter([
        ['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description'],
        ['650703', 'EXECUTED', '2023-09-05T11:30:32Z', '16210', 'SoL', 'PEN', 'Счет 58803664651298323391',
         'Счет 39746506635466619397', 'Перевод организации']
    ])

    result = get_transaction_from_csv_file(os.path.join(DATA_DIR, 'transactions.csv'))
    expected_result = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "SoL",
            "currency_code": "PEN",
            "from": "Счет 58803664651298323391",
            "to": "Счет 39746506635466619397",
            "description": "Перевод организации"
        }
    ]
