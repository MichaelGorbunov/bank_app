from src.masks import get_masked_nums


def mask_bank_data(bank_data: str) -> str:
    """Функция принимает на вход строку с информацией — тип карты/счета и номер карты/счета.
    И возвращает исходную строку с замаскированным номером карты/счета"""
    data_parts = bank_data.split()

    data_parts[-1] = get_masked_nums(data_parts[-1])

    return " ".join(data_parts)
