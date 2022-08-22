from django.urls import re_path, include
from django.urls import include, path
from rest_framework import routers

from api.views import get_orders, receive_data


# router = routers.DefaultRouter()
# router.register(r'^orders', get_orders)
# router.register(r'^enter', receive_data)

urlpatterns = [
    re_path(r'^orders', get_orders),
    re_path(r'^enter', receive_data)
]


# urlpatterns = router.urls