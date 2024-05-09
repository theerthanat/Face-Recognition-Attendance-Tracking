from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def portfoliodetails(request):
    return render(request,'portfolio-details.html')

def portfolio(request):
    return render(request,'portfolio.html')

def resume(request):
    return render(request,'resume.html')

def services(request):
    return render(request,'services.html')

#Projects
def h1_sih(request):
    return render(request,'h1_sih.html')

def h2_tcs(request):
    return render(request,'h2_tcs.html')

def h3_ifa(request):
    return render(request,'h3_ifa.html')

def h4_star(request):
    return render(request,'h4_star.html')

def h5_t1hacks(request):
    return render(request,'h5_t1hacks.html')

def h6_engineersDay(request):
    return render(request,'h6_engineersDay.html')

def h7_participation(request):
    return render(request,'h7_participation.html')