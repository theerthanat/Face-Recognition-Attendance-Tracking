from django.shortcuts import render
from trackingDetails.models import trackers
# Create your views here.

def userList(request):
    #return HttpResponse("Hello world");
    result=trackers.objects.all()
    return render(request,'tracker.html',{'result':result})
