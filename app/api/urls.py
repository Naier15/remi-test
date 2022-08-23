from django.urls import re_path, include
from django.urls import include, path
from rest_framework import routers

from api.views import receive_data, ProductViewSet, get_currency_rates


router = routers.DefaultRouter()
router.register(r'^products', ProductViewSet, 'api-products')

urlpatterns = [
    re_path(r'^enter', receive_data, name='enter'),
    re_path(r'^currency', get_currency_rates, name='currency'),
]


urlpatterns += router.urls