from django.urls import re_path, include
from django.urls import include, path
from rest_framework import routers

from api.views import get_orders


# router = routers.DefaultRouter()
# router.register(r'orders', get_orders)

urlpatterns = [
    re_path(r'^orders', get_orders),
]
