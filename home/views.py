from django.shortcuts import render
from django.http import HttpResponse, request, response
# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def review(request):
    return render(request, 'pages/review.html')

def reviewpost(request):
    return render(request, 'pages/reviewpost.html')

def support(request):
    return render(request, 'pages/support.html')
    
def login(request):
    return render(request, 'pages/createacc.html')

def signin(request):
    return render(request, 'pages/signin.html')

def tourticket(request):
    return render(request, 'pages/tourticket.html')

def moveticket(request):
    return render(request, 'pages/moveticket.html')

def roomticket(request):
    return render(request, 'pages/roomticket.html')

def otherservicesticket(request):
    return render(request, 'pages/otherservicesticket.html')

def order(request):
    return render(request, 'pages/order.html')

def moveticket(request):
    return render(request, 'pages/moveticket.html')

def roomticket(request):
    return render(request, 'pages/roomticket.html')

def areareview(request):
    return render(request, 'pages/areareview.html')