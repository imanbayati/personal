from django.shortcuts import render
from . models import *
# Create your views here.
def home_page(request,cat_name=None):
    categories = Category.objects.all()
    if cat_name != None:
        works = Work.objects.filter(status=1,category__name=cat_name)
    else:
        works = Work.objects.filter(status=1)
    context = {'works':works,'categories':categories}
    return render(request, 'work/home.html',context)

