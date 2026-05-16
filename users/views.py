from django.shortcuts import render, HttpResponse

def person(request):
    return render(request , 'index.html')

