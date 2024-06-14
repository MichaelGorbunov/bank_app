import pytest

from src.masks import get_masked_nums


@pytest.mark.parametrize(
    "number, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("64686473678894779589", "**9589"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("35383033474447895560", "**5560"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_get_masked_nums_correct_data(number: str, expected: str) -> None:
    assert get_masked_nums(number) == expected


def test_get_masked_nums_incorrect_data() -> None:
    assert get_masked_nums("111111111111111111111") == "Введите 16 или 20-значное число"
