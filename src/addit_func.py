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
