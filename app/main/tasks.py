from app.celery import app
from django.utils.timezone import localtime

import requests

from main.utils import Currency


@app.task
def get_currency_rates() -> bool:
    API_URL = 'https://cdn.cur.su/api/nbu.json'

    try:
        resp: dict = requests.get(API_URL).json()
        rates: dict = resp['rates']
        USD_RUB: float = rates.get('RUB')
        EUR_RUB: float = USD_RUB / rates.get('EUR')

        Currency.load(USD_RUB, EUR_RUB)
        return True
    except:
        return False