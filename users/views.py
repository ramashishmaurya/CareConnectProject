from django.shortcuts import render, HttpResponse

def person(request):
    return render(request , 'index.html')

def tweets(request):
    return render(request , 'navbar.html')

def footer(request):
    return render(request ,'footer.html')

def login(request):
    return render(request ,'login.html' )