from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(File)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','phone','email','site','company')
    
admin.site.register(Contact,ContactAdmin)