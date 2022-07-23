from django.shortcuts import render
from . models import Work
# Create your views here.
def home_page(request):
    works = Work.objects.all()
    context = {'works':works}
    return render(request, 'work/home.html',context)