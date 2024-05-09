from django.urls import path
from . import views

urlpatterns=[
    path('login',views.login,name='login'),
    path('createUser',views.createUser,name='createUser'),
    path('signup',views.signup,name='signup'),
    path('checkUsers',views.checkUsers,name='checkUsers')
]