
from src.utils import get_transaction_from_file



# from unittest.mock import Mock
#
# def test_get_transaction_from_file():
#     mock_random = Mock(return_value=5)
#
#     assert get_transaction_from_file("../data/operation.json") == 5
#     mock_random.assert_called_once_with(0, 10)

print(get_transaction_from_file("operation.json"))