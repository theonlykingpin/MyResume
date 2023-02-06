from django.urls import path
from server.views import Landing, Resume


app_name = 'server'

urlpatterns = [
    path('', Landing.as_view(), name='landing'),
    path('resume/', Resume.as_view(), name='resume'),
]
