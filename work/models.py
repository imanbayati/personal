from django.db import models
from django.urls import reverse
# Create your models here.

    
class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img/',default='img/default')
    def __str__(self):
        return self.name
    
class Post(models.Model):
    url = models.CharField(max_length=500,default='https://imanbayati.github')
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='img/',default='img/default.jpg')
    status = models.BooleanField(default=False)
    publish = models.DateTimeField(null=True)
    update = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-publish']
        
    def __str__(self):
        return self.name  
    
    def get_absolute_url(self):
        return reverse('work:home')  
