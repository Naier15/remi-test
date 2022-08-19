from functools import reduce
from re import template
from django.http import HttpResponse
from django.shortcuts import render, redirect
from asgiref.sync import sync_to_async
from django.views.generic import ListView
from django.core.handlers.asgi import ASGIRequest
from django.db.models import Q

from main.models import Product

import asyncio
from time import sleep
import httpx
from main.utils import query_counter


# helpers

# views functions
async def menu(request: ASGIRequest):
    if not request.session.get('basket'):
        request.session['basket'] = {}

    if request.method == 'POST':
        item: dict = request.session['basket'].get(request.POST['id'])
        if not item:
            new_item: dict = {
                'title': request.POST['title'],
                'quantity': 1.0,
                'price': float(request.POST['price'].replace(',', '.')),
                'total': float(request.POST['price'].replace(',', '.')),
                'description': request.POST['description'] if request.POST['description'] != 'None' else None,
                'image': request.POST['image']
            }
            request.session['basket'][request.POST['id']] = new_item
        else:
            item['quantity'] += 1.0
            item['total'] = item['price'] * item['quantity']
            request.session['basket'][request.POST['id']] = item
        request.session.modified = True

    # del request.session['basket'] #Удаляет корзину в сессии
    # print(request.session['basket'])

    if request.session['basket']:
        quantities = (elem['quantity'] for elem in request.session['basket'].values())
        basket_count = round(reduce(lambda x, y: x + y, quantities))
    else:
        basket_count = None

    products = Product.objects.all()
    context = {'menu_active': 'active', 'basket_active': '', 'products': products, 'basket_count': basket_count}
    return render(request, 'main/menu.html', context=context)


async def basket(request: ASGIRequest):
    if not request.session.get('basket'):
        request.session['basket'] = {}

    basket: dict = request.session['basket']

    action = request.POST.get('action', None)
    if action == 'add_one':
        id = request.POST.get('id')

        item = basket[id]
        item['quantity'] += 1.0
        item['total'] += item['price']
        basket[id] = item

        request.session['basket'] = basket

    elif action == 'remove_one':
        id = request.POST.get('id')

        item = basket[id]
        item['quantity'] -= 1.0
        item['total'] -= item['price']

        if item['quantity'] == 0.0:
            del basket[id]
        else:
            basket[id] = item

        request.session['basket'] = basket

    basket = request.session['basket']
    context = {'menu_active': '', 'basket_active': 'active', 'basket': basket}
    return render(request, 'main/basket.html', context=context)



# views classes
# class MenuList(ListView):
#     model = Product
#     template_name = 'main/menu.html'
#     context_object_name = 'products'
#     # extra_context = {'menu_active': 'active', 'basket_active': ''}

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu_active'] = 'active'
#         context['basket_active'] = ''
#         return context

#     def get_queryset(self):
#         return Product.objects.all()

