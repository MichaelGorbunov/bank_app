# import json
from unittest.mock import patch

from src.external_api import currency_conversion


@patch("src.external_api.requests.get")
# @patch('src.read_f.get_user_repos')
def test_currency_conversion(mocked_get):
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 1},
        "info": {"timestamp": 1718255463, "rate": 98.303283},
        "date": "2024-06-13",
        "result": 98.303283,
    }
    result = currency_conversion("EUR", 1.0)
    assert result == 98.303283


# {'success': True, 'query': {'from': 'EUR', 'to': 'RUB', 'amount': 1}, 'info':
# {'timestamp': 1718255463, 'rate': 98.303283}, 'date': '2024-06-13', 'result': 98.303283}


@patch("src.external_api.requests.get")
def test_currency_conversion_invalid(mocked_get):
    mocked_get.return_value.status_code = 404
    # mocked_get.return_value.json.return_value = {}
    result = currency_conversion("EUR", 1.0)
    assert result == (0.00)
