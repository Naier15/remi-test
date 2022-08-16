from django.http import HttpResponse
from django.shortcuts import render
from asgiref.sync import sync_to_async
from django.views.generic import ListView

from main.models import Product

import asyncio
from time import sleep
import httpx


# helpers

# views functions
# async def menu(request):
#     products = Product.objects.all()
#     return render(request, 'main/menu.html', {'menu_active': 'active', 'basket_active': '', 'products': products})

async def basket(request):
    return render(request, 'main/basket.html', {'menu_active': '', 'basket_active': 'active'})


# views classes
class MenuList(ListView):
    model = Product
    template_name = 'main/menu.html'
    context_object_name = 'products'
    # extra_context = {'menu_active': 'active', 'basket_active': ''}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_active'] = 'active'
        context['basket_active'] = ''
        return context

    def get_queryset(self):
        return Product.objects.all()

