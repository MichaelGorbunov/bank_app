import os
from datetime import datetime


def scan_dirs(path: str, recurse: bool = False) -> dict:
    """Функция принисает на фход путь в виде r-строки и возвращает словарь вида:
    {"files": количество файлов в директории, "folders": количество папок в директории}
    Если путь до директории не указан, используется директория,
    в которой расположен файл с этой функцией.
    Функция может принимать необязательный второй параметр, который указывает,
     нужно ли считать вложенные файлы и папки (рекурсивный подсчет).
     По умолчанию рекурсивный подсчет не осуществляется."""

    some_dict = {"files": 0, "folders": 0}

    if not recurse:
        for i in os.scandir(path):
            if i.is_file():
                some_dict["files"] += 1
            elif i.is_dir():
                some_dict["folders"] += 1

    else:
        for path, folder, files in os.walk(path):
            some_dict["files"] += len(files)
            some_dict["folders"] += len(folder)
    return some_dict


def find_adv_string(str_list: list) -> list:
    """функция принимает на вход список строк и возвращает список строк,
    в которых первая и последняя буквы совпадают.
    Если список пустой, возврат пустого списка."""
    return_list = []
    if len(str_list) < 1:
        return_list = str_list
        return return_list
    for item in str_list:
        if item[:1] == item[-1:]:
            return_list.append(item)
    return return_list


def search_max_div(number_list: list[int]) -> int:
    """Функция принимает на вход список целых чисел и возвращает максимальное
    произведение двух чисел из списка.
    Если в списке менее двух чисел, функция  возвращает 0"""
    if len(number_list) < 2:
        return 0
    sort_num_list = sorted(number_list)
    left_div = sort_num_list[0] * sort_num_list[1]
    right_div = sort_num_list[-1] * sort_num_list[-2]
    if left_div <= right_div:
        return right_div
    else:
        return left_div


def select_product(sel_prod_list: list, category: str) -> list:
    """Функция фильтрует список словарей по ключу category"""
    out_sel_list = []
    for item_product in sel_prod_list:
        if item_product["category"] == category:
            out_sel_list.append(item_product)
    return out_sel_list


def sort_dict_list(product_list: list, cat: str | None) -> list:
    """функция, которая принимает на вход список словарей, состоящих из данных о продуктах в магазине.
    Каждый словарь содержит следующие поля:
        name    — название продукта;
        price    — стоимость;
        category    — категория продукта;
        quantity    — количество в наличии.
    Функция должна возвращать список словарей, отсортированных по убыванию стоимости продукта,
    но только для продуктов из заданной категории.
    Если категория не задана, то сортировка производится для всех продуктов."""
    out_prod_list = []
    if len(product_list[0]) == 0:
        return []
    if cat is None:
        out_prod_list = product_list
    else:
        out_prod_list = select_product(product_list, cat)

    sorted_product = sorted(out_prod_list, key=lambda x: x["price"], reverse=True)
    return sorted_product


def sorting_list(raw_list: list) -> list:
    """функция принимает список,подсчитывае сумму в заказе,
    сортирует список по дате и возвращает в виде списка
    значений [{'date': '2024-01', 'sum': 41.5},...]"""
    temp_list = []
    for item in raw_list:
        temp_dic = {}
        date2 = (datetime.strptime(item["date"], "%d.%m.%Y")).strftime("%Y-%m")
        sum1 = 0
        for item2 in item.get("items"):
            sum1 = sum1 + item2["price"] * item2["quantity"]
        temp_dic["date"] = date2
        temp_dic["sum"] = sum1
        temp_list.append(temp_dic)
    return sorted(temp_list, key=lambda x: x["date"])


def summ_price(products: list, category: str) -> dict:
    """функция суммирует значения в указанной категории,возвращает среднее значение,
    и количество вхождений."""
    avg2 = {}
    summ = 0
    count = 0
    for product in products:
        if product["date"] == category:
            summ += product["sum"]
            count += 1
    avg = round(summ / count, 2)
    avg2["average_order_value"] = avg
    avg2["order_count"] = count

    return avg2


def stat_avg_count(stat_list: list) -> dict:
    """функция принимает список словарей,возвращает список словарь
    вида {'2024-01': {'average_order_value': 222.32, 'order_count': 4},
    где указаны средняя сумма заказов,их количество. Ключом выступает месяц"""
    temp_list1 = sorting_list(stat_list)
    avg1 = {}
    data_set1 = []
    for item in temp_list1:
        if not item["date"] in data_set1:
            data_set1.append(item["date"])
    for dates in data_set1:
        avg1[dates] = summ_price(temp_list1, dates)
    return avg1
