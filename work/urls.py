from django.urls import path
from . views import *

app_name = 'work'
urlpatterns = [
    path('', home_page, name='home'),
    path('category/<str:cat_name>', home_page, name='category'),
    path('<int:pid>/',single_page, name='single')
]