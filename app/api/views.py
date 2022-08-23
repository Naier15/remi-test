from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions

from api.serializers import ProductSerializer
from main.models import Peer, Product
from main.utils import Currency


@csrf_exempt
def receive_data(request):
    latitude, longitude = request.POST.get('loc').split(',')
    Peer.objects.create(
        latitude = latitude,
        longitude = longitude,
        city = request.POST.get('city'),
        ip = request.POST.get('ip'),
    )
    return JsonResponse({'status': 'success'})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(quantity__gt=0.0)
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductSerializer

def get_currency_rates(request):
    dollar, euro, minutes, seconds = Currency.dump()
    return JsonResponse({
        'status': 'success',
        'data': {
            'dollar': dollar,
            'euro': euro,
            'minutes': minutes,
            'seconds': seconds
        }})