from django.urls import path
from . import views

urlpatterns=[
    path('userList',views.userList,name='userList')
]