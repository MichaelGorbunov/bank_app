def filter_operations(in_dict_list: list[dict], in_state: str = "EXECUTED") -> list[dict] | None:
    """Функция принимает список словарей с деталями операций и возвращает
    отсортированные по одному из состояний ["EXECUTED", "CANCELED"].
    Сортировкой по умолчанию является "EXECUTED" """
    if in_state not in ["EXECUTED", "CANCELED"]:
        return None
    sort_list = []
    for item in in_dict_list:
        if item.get("state") == in_state:
            # print(item)
            sort_list.append(item)
    return sort_list


def sorted_operation(in_sort_list: list[dict], reverse_direction: bool = True) -> list[dict] :
    """Функцию принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты (ключ date).
    Функция принимает два аргумента, второй необязательный задает
    порядок сортировки (убывание, возрастание)."""
    sorted_list = sorted(in_sort_list, key=lambda item: item["date"], reverse=reverse_direction)
    return sorted_list
