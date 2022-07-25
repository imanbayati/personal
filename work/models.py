from django.db import models


# Create your models here.

    
class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img/',default='img/default')
    def __str__(self):
        return self.name
    
class Work(models.Model):
    file = models.FileField(upload_to='files/',null=True)
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
