from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, request, response
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Area, Customer, Product, Room
# Create your views here.

# def home(request, username):
#     %{username}%
#     return render(request, 'pages/home.html', username=username)
# class Home(View):
#     def get(self, request):
#         username = request.POST.get('username')
#         return render(request, 'pages/home.html', {'username': username})

def home(request):
    products = Product.objects.all()
    areas = Area.objects.all()
    # product = products[0].image
    # print('Debug')
    return render(request, 'pages/home.html', {'products' : products, 'areas': areas})


def review(request):
    areas = Area.objects.all()
    context = {'areas': areas}
    return render(request, 'pages/review.html',context)


def reviewpost(request):
    return render(request, 'pages/reviewpost.html')

def support(request):
    return render(request, 'pages/support.html')

def signin(request):
    return render(request, 'pages/signin.html')

def tourticket(request):
    products = Product.objects.all()
    return render(request, 'pages/tourticket.html',{'products' : products})

def moveticket(request):
    return render(request, 'pages/moveticket.html')

def roomticket(request):
    rooms = Room.objects.all()
    return render(request, 'pages/roomticket.html',{'rooms' : rooms})

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
            user = form.save()
            username = form.cleaned_data.get('username')
            Customer.objects.create(
                user=user,
                name=username,
                email=form.cleaned_data.get('email')
            )

            messages.success(request, 'Account was created')
            return redirect('login_page')
    context = {'form' : form}
    
    return render(request, 'pages/register.html', context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            Customer.objects.create(
                user=user,
                name=username,
                email=form.cleaned_data.get('email')
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'Homepage/register.html', context)

def login_page(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return redirect('home')
            return render(request, 'pages/home.html')
        else: 
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'pages/signin.html', context)
    else:
        logout(request)
    return render(request, 'pages/signin.html', context)

# def logout_user(request):
#     logout(request)
#     return redirect('login')