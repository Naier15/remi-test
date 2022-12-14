from django.urls import re_path, path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'', include('main.urls')),
    re_path(r'^api/v1/', include('api.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


