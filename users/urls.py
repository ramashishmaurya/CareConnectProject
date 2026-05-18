
from django.contrib import admin
from django.shortcuts import HttpResponse
from django.urls import path ,include
from users import views

def home(request):
    return HttpResponse('hello worlds')

urlpatterns = [
    path('person/' ,views.person)  , 
    path('tweets/' ,views.tweets   , name='tweets') ,
    path('footer/' ,views.footer ,name='footer') , 
    path('login/' ,views.login  , name='login') , 
] 