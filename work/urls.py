from django.urls import path
from . views import *

app_name = 'work'
urlpatterns = [
    path('', home_page, name='home'),
]