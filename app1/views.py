from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Destination
# Create your views here.
def home(request):
    #return HttpResponse("Hello world");
    return render(request,'home.html',{'name':'shibin'})

def login(request):
    #return HttpResponse("Hello world");
    return render(request,'login.html')

def add(request):
    lst=[]
    val1 = int(request.POST["num1"])   
    val2 = int(request.POST["num2"]) 
    res= val1+val2   
    val=Destination.objects.all()[:50]
    for i in val:
        lst.append(i.description)  
        print(i.description)
        print(i)
    print(lst)
    return render(request,'result.html',{'result':lst})