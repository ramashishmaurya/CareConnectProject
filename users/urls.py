
from django.contrib import admin
from django.shortcuts import HttpResponse
from django.urls import path ,include
from users import views

def home(request):
    return HttpResponse('hello worlds')

urlpatterns = [
    path('tweets/' ,views.tweets , name='tweets') , 
    path('login/' ,views.login, name='login') , 
    path('footer/' ,views.footer , name='footer') , 
    path('' ,views.tweets_list , name='tweets_list') ,
    path('create/' ,views.tweets_create ,name='tweets_create') , 
    path('<int:tweets_id>/delete/', views.tweets_delete, name='tweets_delete'),
    path('<int:tweets_id>/edit/',views.tweets_edit , name='tweets_edit') , 


]