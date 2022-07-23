from django.urls import path
from . views import *

app_name = 'website'
urlpatterns = [
    path('', home_page, name='home'),
    path('contact', contact_page, name='contact')
]