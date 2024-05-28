from typing import Generator


def card_number_generator(start: int, stop: int) -> list[str] | None:
    """генератор номеров банковских карт в формате
    XXXX XXXX XXXX XXXX в диапазоне от start до stop"""

    if stop < start or stop > 9999999999999999:
        return None

    card_number_list: list[str] = []
    for i in range(start, stop + 1):
        nm = list(str(i).zfill(16))
        nm.insert(4, " ")
        nm.insert(9, " ")
        nm.insert(14, " ")
        card_number_list.append("".join(nm))
    return card_number_list


def filter_by_currency(transactions: list[dict], currency: str = "USD") -> filter:
    """функция принимает список словарей с банковскими
    операциями (или объект-генератор, который выдает по одной банковской операции)
    и возвращает итератор, который выдает по очереди операции,
    в которых указана заданная валюта"""
    filtered_transact = filter(lambda x: x["operationAmount"]["currency"]["name"] == currency, transactions)
    return filtered_transact


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """генератор, который принимает список словарей и возвращает описание каждой операции
    по очереди"""
    for item in transactions:
        yield item["description"]


"""Реализуйте функцию, которая принимает список словарей с банковскими
операциями (или объект-генератор, который выдает по одной банковской операции)
и возвращает итератор, который выдает по очереди операции,
в которых указана заданная валюта.
Пример вызова функции:
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions)["id"])
Пример вывода:

939719570
142264268
Напишите генератор, который принимает список словарей и возвращает описание каждой операции
 по очереди.
Пример вызова функции:
descriptions = transaction_descriptions(transactions):
for _ in range(5):
    print(next(descriptions)

Пример вывода:

Перевод организации
Перевод со счета на счет
Перевод со счета на счет
Перевод с карты на карту
Перевод организации

Напишите генератор номеров банковских карт, который должен генерировать номера карт в формате
XXXX XXXX XXXX XXXX
, где
X
— цифра. Должны быть сгенерированы номера карт в заданном диапазоне,
например от 0000 0000 0000 0001 до 9999 9999 9999 9999
(диапазоны передаются как параметры генератора).
Пример вызова функции:

for card_number in card_number_generator(1, 5):
    print(card_number)

0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
0000 0000 0000 0004
0000 0000 0000 0005"""
