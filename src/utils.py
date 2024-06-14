# Реализуйте функцию, которая принимает на вход путь до JSON-файла
# и возвращает список словарей с данными о финансовых транзакциях.
# Если файл пустой, содержит не список или не найден, функция возвращает пустой список.

# current_dir = os.path.dirname(os.path.abspath(__file__))
# json_file_path = os.path.join(current_dir, "../data", "operations.json")
# list_transactions = data_transactions(json_file_path)
import json

from src.external_api import currency_conversion

# import os.path
# from typing import Dict, List


def get_transaction_from_file(path: str) -> list:
    """функция принимает путь до json файла и возвращает список словарей"""
    blank_list: list = []
    try:
        with open(path, "r", encoding="utf-8") as transaction_file:
            try:
                transaction_data = json.load(transaction_file)
            except json.JSONDecodeError:
                # print("Ошибка декодирования файла")
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
        return 0.0
    # print(transaction)

    if "operationAmount" in transaction:
        currency = transaction["operationAmount"]["currency"]["code"]
        if currency == "RUB":
            return float(transaction["operationAmount"]["amount"])
        elif currency != "RUB":
            # date_transact = transaction["date"][:10]
            # return currency_conversion(currency, transaction["operationAmount"]["amount"], date_transact)
            return currency_conversion(currency, transaction["operationAmount"]["amount"])
    return 0.0
