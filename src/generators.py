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
Напишите генератор, который принимает список словарей и возвращает описание каждой операции по очереди.
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

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def card_number_generator(start: int, stop: int) -> list[str] | None:
    """генератор номеров банковских карт в формате
    XXXX XXXX XXXX XXXX в диапазоне от start до stop"""

    if stop < start or stop > 10000000000000000:
        return None
    card_number_list: list[str] = []
    for i in range(start, stop + 1):
        nm = list(str(i).zfill(16))
        nm.insert(4, " ")
        nm.insert(9, " ")
        nm.insert(14, " ")
        card_number_list.append("".join(nm))
    return card_number_list


# for card_number in card_number_generator(9999999999999998, 9999999999999999):
#     print(card_number)
# тест card_number in card_number_generator
def filter_by_currency(transactions: list[dict], currency: str = "USD") -> filter:
    """функцию принимает список словарей с банковскими
операциями (или объект-генератор, который выдает по одной банковской операции)
и возвращает итератор, который выдает по очереди операции,
в которых указана заданная валюта"""
    filtered_transact = filter(lambda x: x["operationAmount"]["currency"]["name"] == currency, transactions)
    return filtered_transact


print(type(filter_by_currency(transactions)))
usd_transactions = filter_by_currency(transactions)
rub_transactions = filter_by_currency(transactions, "руб.")
for _ in range(3):
    print(next(usd_transactions)["id"])
print("*")
for _ in range(2):
    print(next(rub_transactions)["id"])


def transaction_descriptions(transactions: list[dict]):
    for item in transactions:
        yield item["description"]


descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))
