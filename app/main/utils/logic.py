from functools import reduce
from django.core.handlers.asgi import ASGIRequest
from decimal import Decimal, getcontext


def count_basket_items(basket):
    if basket:
        quantities = (elem['quantity'] for elem in basket.values())
        basket_count = round(reduce(lambda x, y: x + y, quantities))
    else:
        basket_count = None
    return basket_count


def update_basket(POST, item=None):
    if not item:
        item: dict = {
            'title': POST['title'],
            'quantity': 1.0,
            'price': float(POST['price'].replace(',', '.')),
            'total': float(POST['price'].replace(',', '.')),
            'description': POST['description'] if POST['description'] != 'None' else None,
            'image': POST['image']
        }
    else:
        item['quantity'] += 1.0
        item['total'] = item['price'] * item['quantity']
    return item


def basket_action(basket, action, id):
    getcontext().prec = 10

    if action == 'add_one':
        item = basket[id]
        item['quantity'] += 1.0
        item['total'] = float(Decimal(item['total']) + Decimal(item['price']))
        basket[id] = item


    elif action == 'remove_one':
        item = basket[id]
        item['quantity'] -= 1.0
        item['total'] = float(Decimal(item['total']) - Decimal(item['price']))

        if item['quantity'] == 0.0:
            del basket[id]
        else:
            basket[id] = item

    return basket


def calc_total_price(basket):
    getcontext().prec = 10

    res = Decimal('0')
    for values in basket.values():
        res += Decimal(values.get('total'))
    return res