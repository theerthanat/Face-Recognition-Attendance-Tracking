from django.db import models

# Create your models here.
class trackers(models.Model):
    empId=models.CharField(max_length=100,default='EMP0001')
    lastUpdatedBy = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    forKey=models.IntegerField(default=0,blank=True)