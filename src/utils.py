# Реализуйте функцию, которая принимает на вход путь до JSON-файла
# и возвращает список словарей с данными о финансовых транзакциях.
# Если файл пустой, содержит не список или не найден, функция возвращает пустой список.

# current_dir = os.path.dirname(os.path.abspath(__file__))
# json_file_path = os.path.join(current_dir, "../data", "operations.json")
# list_transactions = data_transactions(json_file_path)
import json
import logging
import os
from typing import Any, Dict, List

from config import LOGS_DIR
from src.external_api import currency_conversion

logger = logging.getLogger("utils")

logger_file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "utils.log"), encoding="utf8", mode="w")
logger_formatter = logging.Formatter("%(asctime)s - %(levelname)s - FUNC(%(funcName)s): %(message)s")
logger_file_handler.setFormatter(logger_formatter)
logger.addHandler(logger_file_handler)
logger.setLevel(logging.INFO)


# import os.path


def get_transaction_from_file(path: str) -> list[Dict]:
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
        # print("Файл не найден")
        return blank_list
    return transaction_data


# Реализуйте функцию, которая принимает на вход транзакцию и возвращает
# сумму транзакции (amount) в рублях, тип данных —float.
# Если транзакция была в USD или EUR, происходит обращение к внешнему API
# для получения текущего курса валют и конвертации суммы операции в рубли.
# Для конвертации валюты воспользуйтесь Exchange Rates Data API:
# https://apilayer.com/exchangerates_data-api.
# Функцию конвертации поместите в модульexternal_api


def get_transaction_amount(transaction: dict) -> float:
    """функция возвращает сумму транзакции и при необходимости конвертирует в рубли"""
    if not transaction:
        logger.error("Транзакция не найдена")
        return 0.0
    # print(transaction)

    if "operationAmount" in transaction:
        currency = transaction["operationAmount"]["currency"]["code"]
        if currency == "RUB":
            logger.info(f"Вывод суммы транзакции, если код валюты {currency}")
            return float(transaction["operationAmount"]["amount"])
        elif currency != "RUB":
            logger.info(f"Вывод суммы транзакции, если код валюты {currency}")
            # date_transact = transaction["date"][:10]
            # return currency_conversion(currency, transaction["operationAmount"]["amount"], date_transact)
            return currency_conversion(currency, transaction["operationAmount"]["amount"])
    logger.error("Нет ключа 'operationAmount' в транзакции")
    return 0.0
