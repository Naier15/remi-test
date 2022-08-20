from app.celery import app
import requests

@app.task
def get_currency_rates() -> tuple[float, float]:
    API_URL = 'https://cdn.cur.su/api/nbu.json'

    resp = requests.get(API_URL).json()
    rates = resp['rates']
    USD_RUB = round(rates.get('RUB'), 2)
    EUR_RUB = round(USD_RUB / rates.get('EUR'), 2)
    print(USD_RUB, EUR_RUB)
    return True