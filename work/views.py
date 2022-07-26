from django.shortcuts import render
from . models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home_page(request,cat_name=None):
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    if cat_name != None:
        posts = Post.objects.filter(status=1,category__name=cat_name)

    posts = Paginator(posts,9)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1) 
    context = {'posts':posts,'categories':categories}
    return render(request, 'work/home.html',context)

