from django.shortcuts import render ,HttpResponse 
from django.http import JsonResponse
# Create your views here.
def apiresponse(request):
    data ={
        'name':'ashsish' , 
        'class':10
    }
    return JsonResponse(data=data) # json is accepting the json formate u sending the normla test here 
