import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def currency_conversion(currency: str, sum_transaction: float) -> float:
    # def currency_conversion(currency: str, sum_transaction: float, date_transact: str):
    """Конвертирует валюту через API и возвращает его в виде float"""

    # url = f"https://api.apilayer.com/exchangerates_data/
    # convert?to={'RUB'}&from={currency}&amount={sum_transaction}&date={date_transact}"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={currency}&amount={sum_transaction}"
    try:
        response = requests.get(url, headers={"apikey": API_KEY})
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return 0.00

    response_data = json.loads(response.text)
    return float(response_data["result"])


# print(currency_conversion("EUR", 1.0))
