from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

handler404 = 'core.handlers.handler404'
handler500 = 'core.handlers.handler500'
handler403 = 'core.handlers.handler403'
handler400 = 'core.handlers.handler400'


urlpatterns = [
    path('administrator', admin.site.urls),
    path('', include('server.urls', namespace='server')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
