from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def indexAgency(request):
    return render(request,"index-agency.html")

def indexPortfolio(request):
    return render(request,"index-portfolio.html")

def indexCorporate(request):
    return render(request,"index-corporate.html")

def indexLandingPage(request):
    return render(request,"index-landing.html")
   
def indexBlog(request):
    return render(request,"index-blog.html")

def indexApp(request):
    return render(request,"index-app.html")

def indexRestaurant(request):
    return render(request,"index-restaurant.html")

def indexMinimal(request):
    return render(request,"index-minimal.html")

def indexComingSoon(request):
    return render(request,"index-countdown.html")

def aboutUs(request):
    return render(request,"about-us.html")

def services(request):
    return render(request,"services.html")

def contacts1(request):
    return render(request,"contacts1.html")

def contacts2(request):
    return render(request,"contacts2.html")

def error404(request):
    return render(request,"error404.html")