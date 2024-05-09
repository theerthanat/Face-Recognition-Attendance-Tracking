"""portf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('portfoliodetails/', views.portfoliodetails,name='portfoliodetails'),
    path('portfolio/', views.portfolio,name='portfolio'),
    path('resume/', views.resume,name='resume'),
    path('services/', views.services,name='services'),
    path('h1_sih/', views.h1_sih,name='h1_sih'),
    path('h2_tcs/', views.h2_tcs,name='h2_tcs'),
    path('h3_ifa/', views.h3_ifa,name='h3_ifa'),
    path('h4_star/', views.h4_star,name='h4_star'),
    path('h5_t1hacks/', views.h5_t1hacks,name='h5_t1hacks'),
    path('h6_engineersDay/', views.h6_engineersDay,name='h6_engineersDay'),
    path('h7_participation/', views.h7_participation,name='h7_participation'),
]
