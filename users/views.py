from django.shortcuts import render, HttpResponse
from .models import tweets 
from .forms import tweetsform
from django.shortcuts import get_object_or_404 ,  redirect


def person(request):
    return render(request , 'index.html')

def tweets(request):
    return render(request , 'navbar.html')

def footer(request):
    return render(request ,'footer.html')

def login(request):
    return render(request ,'login.html' )

def chat(request):
    return render(request ,'chat.html')

def tweets_list(request):
    tweets = tweets.objects.all().order_by('-created_at')
    return render(request  , 'tweets_list.html' , {'tweets':tweets})

def tweets_create(request):
    if request.method =='POST':
        form = tweetsform(request.POST , request.FILES)
        if form.is_valid():
            tweets = form.save(commit=False)
            tweets.user = request.user
            tweets.save()
            return redirect('tweets_list')


    else:
        form = tweetsform()
    return render(request , 'tweets_create' ,{'form':form})



