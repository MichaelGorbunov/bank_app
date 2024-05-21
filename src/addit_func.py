import os


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
