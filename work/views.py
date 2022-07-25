from django.shortcuts import render
from . models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home_page(request,cat_name=None):
    categories = Category.objects.all()
    if cat_name != None:
        works = Work.objects.filter(status=1,category__name=cat_name)

    works = Work.objects.filter(status=1)
    works = Paginator(works,9)
    try:
        page_number = request.GET.get('page')
        works = works.get_page(page_number)
    except PageNotAnInteger:
        works = works.get_page(1)
    except EmptyPage:
        works = works.get_page(1)
    context = {'works':works,'categories':categories,'works':works}
    return render(request, 'work/home.html',context)

