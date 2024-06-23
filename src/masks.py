import logging
import os
import re

from config import LOGS_DIR

logger = logging.getLogger("masks")
logger_file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "mask.log"), encoding="utf8", mode="w")
logger_formatter = logging.Formatter("%(asctime)s - %(levelname)s - FUNC(%(funcName)s): %(message)s")
logger_file_handler.setFormatter(logger_formatter)
logger.addHandler(logger_file_handler)
logger.setLevel(logging.INFO)


def mask_card_numbers(nums: str) -> str:
    """Функция маскирует номер карты"""
    logger.info("Маскируем номер карты")
    return f"{nums[:4]} {nums[4:6]}** **** {nums[-4:]}"


def mask_account_numbers(nums: str) -> str:
    """Функция маскирует номер счета"""
    logger.info("Маскируем номер счета")
    return f"**{nums[-4:]}"


def get_masked_nums(nums: int | str) -> str:
    """Функция принимает номер карты или счета и возвращает их замаскированными.
    При ошибочно введенных данных возвращает сообщение об ошибке"""

    nums = str(nums)

    if len(nums) == 16 and nums.isdigit():
        logger.info("введен номер карты")
        return mask_card_numbers(nums)

    elif len(nums) == 20 and nums.isdigit():
        logger.info("введен номер счета")
        return mask_account_numbers(nums)

    else:
        logger.error("некорректные данные")
        return "Введите 16 или 20-значное число"


def get_masked_nums2(nums: str) -> str:
    """Функция принимает номер карты или счета и возвращает их замаскированными.
    При ошибочно введенных данных возвращает сообщение об ошибке"""

    matches = re.search(r"(\d{16})|(\d{20})", nums)
    nums = matches.group()

    if len(nums) == 16 and nums.isdigit():
        logger.info("введен номер карты")
        return mask_card_numbers(nums)

    elif len(nums) == 20 and nums.isdigit():
        logger.info("введен номер счета")
        return mask_account_numbers(nums)

    else:
        logger.error("некорректные данные")
        return "Введите 16 или 20-значное число"


# text = "Visa Classic 6831982476737658"
# print(get_masked_nums2(text))
