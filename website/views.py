from django.shortcuts import render
from . models import *
from . forms import ContactForm
from django.contrib import messages
from work.models import *
# Create your views here.
def home_page(request):
    posts = Post.objects.filter(status=1)[:6]
    files = File.objects.all()
    context = {'files': files,'posts':posts}
    return render(request, 'website/home.html',context)

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
           form.save() 
           messages.add_message(request, messages.SUCCESS, 'پیام شما با موفقیت ثبت شد')
        else:
            messages.add_message(request, messages.ERROR, 'متاسفانه پیام شما دریافت نشد')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'website/contact.html',context)