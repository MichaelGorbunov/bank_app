from src.masks import get_masked_nums
from src.utils import get_transaction_amount

test_dict = {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431",
}
print(get_transaction_amount(test_dict))
print(get_transaction_amount({}))

print(get_masked_nums("41421565395219882431"))
print(get_masked_nums("6831982476737658"))
print(get_masked_nums("6831erwerwrw37658"))
