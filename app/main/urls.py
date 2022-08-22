from django.contrib import admin
from django.urls import re_path

from main.views import *


urlpatterns = [
    re_path(r'^$', menu, name='menu'),
    re_path(r'^basket', basket, name='basket'),
    re_path(r'^pay_basket', basket, name='pay_basket'),
    re_path(r'^admin', admin.site.urls),
]