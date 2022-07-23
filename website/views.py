from django.shortcuts import render
from . models import *
from . forms import ContactForm
# Create your views here.
def home_page(request):
    files = File.objects.all()
    context = {'files': files}
    return render(request, 'website/home.html',context)

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
           form.save() 
    form = ContactForm()
    context = {'form': form}
    return render(request, 'website/contact.html',context)