
from django.contrib import admin
from django.shortcuts import HttpResponse
from django.urls import path ,include
from users import views

def home(request):
    return HttpResponse('hello worlds')

urlpatterns = [
    path('' ,views.person)  ,  # this is function is called here rediret with the otherwebsite as well like u should go on this this is what mean here likr    
]