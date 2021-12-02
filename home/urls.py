from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('review', views.review),
    path('postdanang',views.reviewpost),
    path('support',views.support),
    path('register',views.register_page),
    path('signin',views.login_page),
    path('tourticket',views.tourticket),
    path('moveticket',views.moveticket),
    path('roomticket',views.roomticket),
    path('otherservicesticket',views.otherservicesticket),
    path('order',views.order),
    path('moveticket',views.moveticket),
    path('roomticket',views.roomticket),
    path('areareview',views.areareview),
    path('dattourhcm',views.dattourhcm),
    path('contact',views.contact) 

]
