from django.shortcuts import render
from . models import *
# Create your views here.
def home_page(request):
    files = File.objects.all()
    context = {'files': files}
    return render(request, 'website/home.html',context)