from django.shortcuts import render
from django.http import HttpResponse, request, response
# Create your views here.

def index(request):
    return render(request, 'pages/home.html')

def review(request):
    return render(request, 'pages/review.html')

def reviewpost(request):
    return render(request, 'pages/reviewpost.html')