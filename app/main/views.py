from django.shortcuts import render
from django.core.handlers.asgi import ASGIRequest
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import ListView
from elasticsearch_dsl import Q
from django.http import HttpResponse

from main.documents import ProductDocument
from main.models import Product
from main.utils import query_counter, Currency, count_basket_items, \
                        update_basket, basket_action, calc_total_price

        
class ExtraDataMixin:
    @classmethod
    def initialize(cls, request):
        if not request.session.get('basket'):
            request.session['basket'] = {}

    @classmethod
    def get_extra_data(cls, request):
        basket: dict = request.session['basket']
        basket_count = count_basket_items(basket)
        dollar, euro, minutes, seconds = Currency.dump()
        return {
            'basket_count': basket_count,
            'dollar': dollar,
            'euro': euro,
            'minutes': minutes,
            'seconds': seconds,
        }

# views functions
async def menu(request: ASGIRequest):
    ExtraDataMixin.initialize(request)
    
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
    ExtraDataMixin.initialize(request)

    if request.method == 'POST':
        basket: dict = request.session['basket']
        action = request.POST.get('action', None)
        id = request.POST.get('id')
        request.session['basket'] = basket_action(basket, action, id)

    basket: dict = request.session['basket']
    total_price = calc_total_price(basket)
    extra_data = ExtraDataMixin.get_extra_data(request)

    context = {'menu_active': '',
                'basket_active': 'active',
                'basket': request.session['basket'],
                'total_price': round(total_price, 2),
                **extra_data
    }
    return render(request, 'main/basket.html', context=context)


class SearchMenu(ExtraDataMixin, ListView):
    template_name = 'main/menu.html'
    document_class = ProductDocument

    def generate_q_expression(self, query):
        return Q(
            'multi_match',
            query=query,
            fields=[
                'title',
                'description'
            ],
            fuzziness='auto'
        )

    def get(self, request, *args, **kwargs):
        try:
            query = request.GET.get('search')
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()

            print(f'[INFO] Found {response.hits.total.value} hit(s) for query: "{query}"')

            extra_data = self.get_extra_data(self.request)
            context = {
                'products': search,
                **extra_data
            }
            return render(request, self.template_name, context)
        except Exception as e:
            return HttpResponse(e, status=500)
