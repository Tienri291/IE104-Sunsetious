from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, request, response
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *

from django.utils import timezone
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
    moves = Move.objects.all()
    return render(request, 'pages/moveticket.html',{'moves' : moves})

def roomticket(request):
    rooms = Room.objects.all()
    return render(request, 'pages/roomticket.html',{'rooms' : rooms})

def otherservicesticket(request):
    return render(request, 'pages/otherservicesticket.html')

import datetime

import json

from django.core import serializers

def order(request, slug):
    product = Product.objects.get(slug = slug)
    vouchers = Voucher.objects.all()
    serialized_vouchers = serializers.serialize("json", Voucher.objects.all())
    if request.method == 'POST':
        customer = \
            request.user.customer if \
                request.user.is_authenticated else Customer.objects.create(
                    user=None, 
                    email=request.POST['email'], 
                    name=request.POST['name'], 
                    phone_number=request.POST['phone']
                )
        voucher = request.POST['voucher']
        order_item = OrderItem.objects.create(
            product=product,
            quantity=request.POST['quantity'],
            voucher=Voucher.objects.get(code=voucher) if voucher else None
        )
        Order.objects.create(
            customer=customer,
            date_order=timezone.now(),
            order_item=order_item,
            complete=True,
            transaction_id=int(datetime.datetime.now().timestamp()),
            payment_option=request.POST['pay']
        )
        messages.success(request, 'Order completed!')
        redirect('home')


    return render(request, 'pages/order.html', context={
        'product': product, 
        'vouchers': vouchers, 
        'serialized_vouchers': serialized_vouchers
    })

# def processOrder(request):
#     transaction_id = datetime.datetime.now().timestamp()
#     data = json.loads(request.body)   
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#     else:
#         print('User not logged in...')
#         print('COOKIES:', request.COOKIES)
#         name = data['form']['name']
#         email = data['form']['email']

#         cookieData = cookieCart(request)
#         items = cookieData['items']
#         customer, created = Customer.objects.get_or_create(
#             email=email,
#         )
#         customer.name = name
#         customer.save()

#         order = Order.objects.create(
#             customer=customer,
#             complete=False,
#         )

#         for item in items:
#             print((item))
#             product = Product.objects.get(id=item['product']['id'])
#             orderItem = OrderItem.objects.create(
#                 product=product,
#                 order=order,
#                 quantity=item['quantity']
#             )
#     total = data['form']['total']
#     order.transaction_id = transaction_id
#     order.complete = True

#     if total == order.get_cart_total:
#         order.complete = True
#     order.save()
#     ShippingAddress.objects.create(
#         customer=customer,
#         order=order,
#         address=data['shipping']['address'],
#         city=data['shipping']['city'],
#         phone=data['shipping']['phone']
#     )
#     return JsonResponse('Payment complete', safe=False)

def areareview(request):
    return render(request, 'pages/areareview.html')

def dattourhcm(request, slug):
    context = {}
    # if slug:
    product =  Product.objects.get(slug = slug)
    info_dd = product.info_dd
    product.info_dd = info_dd.split('.')
    context['product'] = product
    return render(request, 'pages/dattour.html', context=context)

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

def login_page(request):
    if request.method == 'POST':
        if 'logout' not in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else: 
                messages.info(request, 'Username or password is incorrect')
                return render(request, 'pages/signin.html')
        else:
            logout(request)
        
    return render(request, 'pages/signin.html')

# def logout_user(request):
#     logout(request)
#     return redirect('login')