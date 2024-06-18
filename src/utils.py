# Реализуйте функцию, которая принимает на вход путь до JSON-файла
# и возвращает список словарей с данными о финансовых транзакциях.
# Если файл пустой, содержит не список или не найден, функция возвращает пустой список.

import csv
# current_dir = os.path.dirname(os.path.abspath(__file__))
# json_file_path = os.path.join(current_dir, "../data", "operations.json")
# list_transactions = data_transactions(json_file_path)
import json
import logging
import os
from typing import Any, Dict

import pandas as pd

from config import DATA_DIR, LOGS_DIR
from src.external_api import currency_conversion

logger = logging.getLogger("utils")

logger_file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "utils.log"), encoding="utf8", mode="w")
logger_formatter = logging.Formatter("%(asctime)s - %(levelname)s - FUNC(%(funcName)s): %(message)s")
logger_file_handler.setFormatter(logger_formatter)
logger.addHandler(logger_file_handler)
logger.setLevel(logging.INFO)


# import os.path


def get_transaction_from_file(path: str) -> list[Dict] | Any:
    """функция принимает путь до json файла и возвращает список словарей"""
    blank_list: list = []
    try:
        logger.info("Открытие JSON-файла")
        with open(path, "r", encoding="utf-8") as transaction_file:
            try:
                logger.info("Получение списка данными о транзакциях")
                transaction_data = json.load(transaction_file)
            except json.JSONDecodeError:
                # print("Ошибка декодирования файла")
                logger.error("Ошибка обработки файла")
                return blank_list
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path} not found")
        return blank_list
    return transaction_data


# Реализуйте функцию, которая принимает на вход транзакцию и возвращает
# сумму транзакции (amount) в рублях, тип данных —float.
# Если транзакция была в USD или EUR, происходит обращение к внешнему API
# для получения текущего курса валют и конвертации суммы операции в рубли.
# Для конвертации валюты воспользуйтесь Exchange Rates Data API:
# https://apilayer.com/exchangerates_data-api.
# Функцию конвертации поместите в модульexternal_api


def get_transaction_amount(transaction: Dict) -> float:
    """функция возвращает сумму транзакции и при необходимости конвертирует в рубли"""
    if not transaction:
        logger.error("Транзакция не найдена")
        return 0.0
    # print(transaction)

    if "operationAmount" in transaction:
        # currency = transaction["operationAmount"]["currency"]["code"]
        # get('key1', {}).get('key2')
        currency = transaction["operationAmount"].get("currency").get("code")
        if currency == "RUB":
            logger.info(f"Вывод суммы транзакции, если код валюты {currency}")
            return float(transaction["operationAmount"].get("amount"))
        elif currency != "RUB":
            logger.info(f"Вывод суммы транзакции, если код валюты {currency}")
            # date_transact = transaction["date"][:10]
            # return currency_conversion(currency, transaction["operationAmount"]["amount"], date_transact)
            return currency_conversion(currency, transaction["operationAmount"].get("amount"))
    logger.error("Нет ключа 'operationAmount' в транзакции")
    return 0.0


def get_transaction_from_csv_file(path: str) -> list[Dict] | Any:
    """функция принимает путь до csv файла и возвращает список словарей"""
    blank_list: list = []
    try:
        with open(path, "r", encoding="UTF-8") as file:
            reader = csv.reader(file, delimiter=";")
            header = next(reader)
            result = []
            for row in reader:
                # print(row)
                row_dict = {
                    "id": row[header.index("id")],
                    "state": row[header.index("state")],
                    "date": row[header.index("date")],
                    "operationAmount": {
                        "amount": row[header.index("amount")],
                        "currency": {
                            "name": row[header.index("currency_name")],
                            "code": row[header.index("currency_code")],
                        },
                    },
                    "description": row[header.index("description")],
                    "from": row[header.index("from")],
                    "to": row[header.index("to")],
                }
                result.append(row_dict)
            file.close()

            return result
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path} not found")
        return blank_list


def get_transaction_from_xlsx_file(path: str) -> list[Dict] | Any:
    """функция извлекает транзакции из файла xlsx"""
    blank_list: list = []
    try:
        df = pd.read_excel(path)
        result = df.apply(
            lambda row: {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "operationAmount": {
                    "amount": row["amount"],
                    "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                },
                "description": row["description"],
                "from": row["from"],
                "to": row["to"],
            },
            axis=1,
        ).tolist()
        return result
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path} not found")
        return blank_list


if __name__ == "__main__":
    print(get_transaction_from_csv_file(os.path.join(DATA_DIR, "test.csv")))
    print(get_transaction_from_xlsx_file(os.path.join(DATA_DIR, "transactions_excel.xlsx")))
