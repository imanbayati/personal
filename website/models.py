from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/files')
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    site = models.CharField(max_length=200,null=True)
    company = models.CharField(max_length=200,null=True)
    content = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.content