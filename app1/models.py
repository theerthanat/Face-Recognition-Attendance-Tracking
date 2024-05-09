from django.db import models

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=100,default='def')
    img=models.ImageField(upload_to='pics', default='pics/default.png')
    description = models.TextField(blank=True,default='def')
    price = models.IntegerField(default=0)
    offer=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)