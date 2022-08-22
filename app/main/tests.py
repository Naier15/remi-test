from main.utils import count_basket_items, update_basket, calc_total_price, basket_action

import pytest
from decimal import Decimal


@pytest.mark.django_db
def test_count_basket_items():
    basket = {'9': {'title': 'Товар №9', 'quantity': 1.0, 'price': 506.28, 'total': 506.28}, 
              '1': {'title': 'Товар №1', 'quantity': 1.0, 'price': 1400.85, 'total': 1400.85}
    }
    assert count_basket_items(basket) == 2

@pytest.mark.django_db
def test_update_basket():
    POST = {'title': ['Товар №9'], 'id': ['9'], 'quantity': ['8,0'], 'price': ['506,28'], } 
    item = {'title': 'Товар №9', 'quantity': 1.0, 'price': 506.28, 'total': 506.28 }
    res = update_basket(POST, item)
    assert res == {'title': 'Товар №9', 'quantity': 2.0, 'price': 506.28, 'total': 1012.56 }

@pytest.mark.django_db
def test_basket_action():
    basket = {'9': {'title': 'Товар №9', 'quantity': 3.0, 'price': 506.28, 'total': 1518.84 }}
    new_basket = {'9': {'title': 'Товар №9', 'quantity': 4.0, 'price': 506.28, 'total': 2025.12 }}
    assert basket_action(basket, 'add_one', '9') == new_basket

@pytest.mark.django_db
def test_calc_total_price():
    basket = {'9': {'title': 'Товар №9', 'quantity': 3.0, 'price': 506.28, 'total': 1518.84 }}
    assert calc_total_price(basket) == Decimal('1518.84')
