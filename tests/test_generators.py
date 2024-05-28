import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_transaction_descriptions(transaction_list: list[dict]) -> None:
    generator = transaction_descriptions(transaction_list)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"


@pytest.mark.parametrize(
    "start,stop, expected_result",
    [
        (2, 1, None),
        (9999999999999999, 10000000000000000, None),
    ],
)
def test_card_number_generator_wrong(start: int, stop: int, expected_result: list[str]) -> None:
    assert card_number_generator(start, stop) == expected_result


@pytest.mark.parametrize(
    "start,stop, expected_result",
    [
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator_good(start: int, stop: int, expected_result: list[str]) -> None:
    assert card_number_generator(start, stop) == expected_result


def test_filter_by_currency_usd(transaction_list: list[dict]) -> None:
    generator = filter_by_currency(transaction_list, "USD")
    assert next(generator)["id"] == 939719570
    assert next(generator)["id"] == 142264268
    assert next(generator)["id"] == 895315941


def test_filter_by_currency_rub(transaction_list: list[dict]) -> None:
    generator = filter_by_currency(transaction_list, "руб.")
    assert next(generator)["id"] == 873106923
    assert next(generator)["id"] == 594226727
