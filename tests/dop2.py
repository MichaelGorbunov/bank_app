# from datetime import datetime
from src.addit_func import stat_avg_count

# Функция должна возвращать словарь, содержащий информацию о средней стоимости заказа и
# количестве заказов за каждый месяц. Ключами словаря должны быть год и месяц в формате
# YYYY-MM
# , а значениями — словари, содержащие два поля:
# average_order_value
# — средняя стоимость заказа за месяц,
# order_count
# — количество заказов за месяц.
list1 = [
    {
        "id": 1,
        "date": "01.01.2024",
        "items": [
            {"name": "tovar1", "price": 10.5, "quantity": 1},
            {"name": "tovar3", "price": 10.6, "quantity": 1},
            {"name": "tovar5", "price": 10.2, "quantity": 2},
        ],
    },
    {
        "id": 2,
        "date": "01.02.2024",
        "items": [{"name": "tovar2", "price": 10.5, "quantity": 2}, {"name": "tovar8", "price": 10.3, "quantity": 1}],
    },
    {"id": 3, "date": "01.03.2024", "items": [{"name": "tovar3", "price": 10.6, "quantity": 1}]},
    {"id": 4, "date": "01.04.2024", "items": [{"name": "tovar1", "price": 10.5, "quantity": 3}]},
    {"id": 5, "date": "01.05.2024", "items": [{"name": "tovar2", "price": 10.7, "quantity": 1}]},
    {"id": 6, "date": "01.06.2024", "items": [{"name": "tovar1", "price": 10.5, "quantity": 1}]},
    {
        "id": 7,
        "date": "01.07.2024",
        "items": [{"name": "tovar5", "price": 10.2, "quantity": 2}, {"name": "tovar8", "price": 10.3, "quantity": 1}],
    },
    {"id": 8, "date": "01.08.2024", "items": [{"name": "tovar1", "price": 10.5, "quantity": 1}]},
    {
        "id": 9,
        "date": "01.09.2024",
        "items": [
            {"name": "tovar8", "price": 10.3, "quantity": 1},
            {"name": "tovar7", "price": 10.5, "quantity": 1},
            {"name": "tovar15", "price": 10.5, "quantity": 2},
        ],
    },
    {"id": 10, "date": "01.01.2024", "items": [{"name": "tovar1", "price": 10.5, "quantity": 1}]},
    {
        "id": 11,
        "date": "01.02.2024",
        "items": [{"name": "tovar1", "price": 10.4, "quantity": 2}, {"name": "tovar7", "price": 10.5, "quantity": 1}],
    },
    {"id": 12, "date": "01.03.2024", "items": [{"name": "tovar7", "price": 10.5, "quantity": 1}]},
    {
        "id": 13,
        "date": "01.04.2024",
        "items": [{"name": "tovar1", "price": 10.9, "quantity": 5}, {"name": "tovar15", "price": 10.5, "quantity": 2}],
    },
    {"id": 14, "date": "01.01.2024", "items": [{"name": "tovar11", "price": 10.8, "quantity": 1}]},
    {
        "id": 15,
        "date": "01.09.2024",
        "items": [
            {"name": "tovar12", "price": 10.5, "quantity": 1},
            {"name": "tovar12", "price": 10.5, "quantity": 1},
        ],
    },
    {"id": 16, "date": "01.11.2024", "items": [{"name": "tovar7", "price": 10.6, "quantity": 5}]},
    {"id": 17, "date": "01.12.2024", "items": [{"name": "tovar18", "price": 10.5, "quantity": 1}]},
    {"id": 18, "date": "01.08.2024", "items": [{"name": "tovar1", "price": 10.7, "quantity": 1}]},
    {"id": 19, "date": "01.07.2024", "items": [{"name": "tovar15", "price": 10.5, "quantity": 2}]},
    {
        "id": 20,
        "date": "01.01.2024",
        "items": [{"name": "tovar9", "price": 102, "quantity": 8}, {"name": "tovar12", "price": 10.5, "quantity": 1}],
    },
    {"id": 21, "date": "01.02.2024", "items": [{"name": "tovar8", "price": 10.1, "quantity": 1}]},
    {"id": 22, "date": "01.03.2024", "items": [{"name": "tovar7", "price": 10.3, "quantity": 1}]},
    {"id": 23, "date": "01.04.2024", "items": [{"name": "tovar11", "price": 10.2, "quantity": 2}]},
]
# temp_list = []
# for item in list1:
#     temp_dic = {}
#     # print("*")
#     # print(item)
#     date2 = (datetime.strptime(item["date"], "%d.%m.%Y")).strftime("%Y-%m")
#     sum = 0
#     for item2 in item.get("items"):
#         sum = sum + item2["price"] * item2["quantity"]
#         # print(item2["price"]*item2["quantity"])
#     # print(sum)
#     temp_dic["date"] = date2
#     temp_dic["sum"] = sum
#     temp_list.append(temp_dic)
#
# temp_list1 = sorted(temp_list, key=lambda x: x["date"])
# print(temp_list1)


# def summ_price(products: list, category: list) -> dict:
#     avg2 = {}
#     summ = 0
#     count = 0
#     for product in products:
#         if product["date"] == category:
#             summ += product["sum"]
#             count += 1
#     avg = round(summ / count, 2)
#     avg2["average_order_value"] = avg
#     avg2["order_count"] = count
#
#     return avg2


# def average_price_per_category(products: list) -> dict:
#     avg1 = {}
#     data_set1 = []
#     for item in temp_list1:
#         if not item["date"] in data_set1:
#             data_set1.append(item["date"])
#     for dates in data_set1:
#         avg1[dates] = summ_price(products, dates)
#     return avg1
#
#
# print(average_price_per_category(temp_list1))


# {
# 'месяц1': {'average_order_value': x1, 'order_count': y1}
# 'месяц2': {'average_order_value': x2, 'order_count': y2}
# 'месяц3': {'average_order_value': x3, 'order_count': y3}
# 'месяц4': {'average_order_value': x4, 'order_count': y4}
# 'месяц5': {'average_order_value': x5, 'order_count': y5}
# ....
# }


# def sorting_list(raw_list:list) -> list:
#     '''функция принимает список,подсчитывае сумму в заказе,
#     сортирует список по дате и возвращает в виде списка
#     значий [{'date': '2024-01', 'sum': 41.5},...]'''
#     temp_list = []
#     for item in raw_list:
#         temp_dic = {}
#         date2 = (datetime.strptime(item["date"], "%d.%m.%Y")).strftime("%Y-%m")
#         sum = 0
#         for item2 in item.get("items"):
#             sum = sum + item2["price"] * item2["quantity"]
#         temp_dic["date"] = date2
#         temp_dic["sum"] = sum
#         temp_list.append(temp_dic)
#     return sorted(temp_list, key=lambda x: x["date"])
#
# def summ_price(products: list, category) -> dict:
#     '''функция суммирует значения в указанной категории,возвращает среднее значение,
#     и количество вхождений.'''
#     avg2 = {}
#     summ = 0
#     count = 0
#     for product in products:
#         if product["date"] == category:
#             summ += product["sum"]
#             count += 1
#     avg = round(summ / count, 2)
#     avg2["average_order_value"] = avg
#     avg2["order_count"] = count
#
#     return avg2
#
#
# def stat_avg_count(stat_list: list) -> dict:
#     '''функция принимает список словарей,возвращает список словарь
#      вида {'2024-01': {'average_order_value': 222.32, 'order_count': 4},
#      где указаны средняя сумма заказов,их количество. Ключом выступает месяц'''
#     temp_list1=sorting_list(stat_list)
#     avg1 = {}
#     data_set1 = []
#     for item in temp_list1:
#         if not item["date"] in data_set1:
#             data_set1.append(item["date"])
#     for dates in data_set1:
#         avg1[dates] = summ_price(temp_list1, dates)
#     return avg1


# tmpList2=[]
# tmpList2=sorting_list(list1)
# print(tmpList2)
tmplist3 = stat_avg_count(list1)
print(tmplist3)
