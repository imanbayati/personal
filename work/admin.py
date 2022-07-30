from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Post)

admin.site.register(Category)
class CommentFormAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email','post']
admin.site.register(Comment,CommentFormAdmin)