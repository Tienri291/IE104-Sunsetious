from django.shortcuts import render, redirect
from django.http import HttpResponse, request, response
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Customer
# Create your views here.

# def home(request, username):
#     %{username}%
#     return render(request, 'pages/home.html', username=username)
# class Home(View):
#     def get(self, request):
#         #username = request.POST.get('username')
#         context = {}
#         return render(request, 'pages/home.html', context)

def home(request):
    return render(request, 'pages/home.html')


def review(request):
    return render(request, 'pages/review.html')

def reviewpost(request):
    return render(request, 'pages/reviewpost.html')

def support(request):
    return render(request, 'pages/support.html')

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

def areareview(request):
    return render(request, 'pages/areareview.html')

def dattourhcm(request):
    return render(request, 'pages/dattour.html')

def contact(request):
    return render(request, 'pages/contact.html')

def cart(request):
    return render(request, 'pages/cart.html')

def register_page(request):
    form = None
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            attrs = form.cleaned_data
            password = attrs['password1']
            del attrs['password1']; del attrs['password2']
            user = Customer(**attrs)
            user.save()
            messages.success(request, 'Account was created')
            return redirect('login_page')
    context = {'form' : form}
    
    return render(request, 'pages/register.html', context)

        
def login_page(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('')
        else: 
            messages.info(request, 'Username or password is incorrect')
            return render(request, '', context)
    return render(request,)
