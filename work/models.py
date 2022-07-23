from django.db import models

# Create your models here.
class Work(models.Model):
    name = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='img/',default='img/default.jpg')
    content = models.TextField()
    status = models.BooleanField(default=False)
    publish = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.name    
