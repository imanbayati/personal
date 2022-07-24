from django.shortcuts import render
from . models import *
# Create your views here.
def home_page(request):
    works = Work.objects.filter(status=1)
    context = {'works':works}
    return render(request, 'work/home.html',context)

def single_page(request,pid):
    works = Work.objects.filter(status=1,id=pid)
    context = {'works':works}
    return render(request, 'work/single.html',context)
