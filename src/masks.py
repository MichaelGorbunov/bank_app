def mask_card_numbers(nums: str) -> str:
    """Функция маскирует номер карты"""
    return f"{nums[:4]} {nums[4:6]}** **** {nums[-4:]}"


def mask_account_numbers(nums: str) -> str:
    """Функция маскирует номер счета"""
    return f"**{nums[-4:]}"


def get_masked_nums(nums: int | str) -> str:
    """Функция принимает номер карты или счета и возвращает их замаскированными.
    При ошибочно введенных данных возвращает сообщение об ошибке"""

    nums = str(nums)

    if len(nums) == 16 and nums.isdigit():
        return mask_card_numbers(nums)

    elif len(nums) == 20 and nums.isdigit():
        return mask_account_numbers(nums)

    else:
        return "Введите 16 или 20-значное число"
