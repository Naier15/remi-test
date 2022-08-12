from django.contrib import admin
from django.urls import re_path

from main.views import index, async_view, sync_view, test


urlpatterns = [
    re_path(r'^$', index),
    re_path(r'^test', test),
    re_path(r'^admin', admin.site.urls),
    re_path(r'^async', async_view),
    re_path(r'^sync', sync_view),
]