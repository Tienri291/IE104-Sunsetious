from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('review/', views.review),
    path('postdanang/',views.reviewpost),
    path('support/',views.support),
    path('login/',views.login),
    path('signin/',views.signin),
    path('tourticket',views.tourticket),
    path('moveticket',views.moveticket),
    path('roomticket',views.roomticket),
    path('otherservicesticket',views.otherservicesticket),
    path('order',views.order),
    path('moveticket',views.moveticket),
    path('roomticket',views.roomticket) 

]
