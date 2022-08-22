from django.shortcuts import render
from django.core.handlers.asgi import ASGIRequest
from django.db.models import Q
from django.core.paginator import Paginator

from main.models import Product
from main.utils import query_counter, Currency, count_basket_items, \
                        update_basket, basket_action, calc_total_price


def initialize(request):
    if not request.session.get('basket'):
        request.session['basket'] = {}
        

# views functions
async def menu(request: ASGIRequest):
    initialize(request)
    
    if request.method == 'POST':
        item: dict = request.session['basket'].get(request.POST['id'])
        item = update_basket(request.POST, item)
        request.session['basket'][request.POST['id']] = item
        request.session.modified = True

    # del request.session['basket'] #Удаляет корзину в сессии
    # print(request.session['basket'])

    basket: dict = request.session['basket']
    basket_count = count_basket_items(basket)

    products = Product.objects.filter(quantity__gt=0.0)
    paginator = Paginator(products, 9)
    page_number = int(request.GET.get('page', 1))
    products = paginator.get_page(page_number)

    dollar, euro, minutes, seconds = Currency.dump()
    context = {'menu_active': 'active', 
                'basket_active': '', 
                'products': products, 
                'basket_count': basket_count,
                'dollar': dollar,
                'euro': euro,
                'minutes': minutes,
                'seconds': seconds,
                'page_range': paginator.page_range,
                'current_page': page_number,
    }
    return render(request, 'main/menu.html', context=context)


async def basket(request: ASGIRequest):
    initialize(request)

    if request.method == 'POST':
        basket: dict = request.session['basket']
        action = request.POST.get('action', None)
        id = request.POST.get('id')
        request.session['basket'] = basket_action(basket, action, id)

    dollar, euro, minutes, seconds = Currency.dump()
    basket: dict = request.session['basket']
    total_price = calc_total_price(basket)

    context = {'menu_active': '',
                'basket_active': 'active',
                'basket': request.session['basket'],
                'dollar': dollar,
                'euro': euro,
                'minutes': minutes,
                'seconds': seconds,
                'total_price': round(total_price, 2),
    }
    return render(request, 'main/basket.html', context=context)