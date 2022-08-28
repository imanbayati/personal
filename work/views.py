from django.shortcuts import render,get_object_or_404
from . models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . forms import CommentForm
from django.contrib import messages

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

def single_page(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'پیام شما با موفقیت ثبت شد')
        else:
            messages.add_message(request, messages.ERROR, 'متاسفانه پیام شما دریافت نشد')
    form = CommentForm()
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,id=pid)
    comments = Comment.objects.filter(post=post.id,approved=True)
    categories = Category.objects.all()
    context = {'post':post,'form':form,'comments':comments,'categories':categories}
    return render(request, 'work/single.html',context)

