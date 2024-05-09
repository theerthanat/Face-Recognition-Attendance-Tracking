from django.db import models

# Create your models here.
class UserDetails(models.Model):
    empId=models.CharField(max_length=7,default='EMP0001')
    empFirstName=models.CharField(max_length=50,default='First Name')
    empLastName=models.CharField(max_length=50,default='Last Name',blank=True)
    empUserName=models.CharField(max_length=100,default='shibint85@gmail.com')
    empAge= models.IntegerField(default=0,blank=True)
    empDOB=models.DateTimeField(blank=True)
    empGender=models.CharField(max_length=1,default='M',blank=True)
    empAddress=models.CharField(max_length=1000,default='address',blank=True)
    empPhone=models.CharField(max_length=10,default='0000000000',blank=True)
    password=models.CharField(max_length=50,default='password')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)