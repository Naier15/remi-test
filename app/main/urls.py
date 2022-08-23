from django.contrib import admin
from django.urls import re_path
from django.views.generic import TemplateView

from main.views import *


urlpatterns = [
    re_path(r'^$', menu, name='menu'),
    re_path(r'^search', SearchMenu.as_view(), name='search'),
    re_path(r'^basket', basket, name='basket'),
    re_path(r'^pay_basket', basket, name='pay_basket'),
    re_path(r'^admin', admin.site.urls),
    re_path(r'^vue', TemplateView.as_view(template_name="main/index.html")),
]