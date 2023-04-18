from django.shortcuts import render, redirect
from .models import * 
from .forms import *

def index(request):
    ad = news.objects.order_by('-time_create')[:5]
    print(request.user)
    form = CreateNewNews()
    if request.method == 'POST':
        form = CreateNewNews(request.POST)
        if request.user.is_authenticated and form.is_valid:
            
            #form.author = request.user
            post = form.save(commit=False)
            post.author = request.user
            post.save()

    context ={
        'ad':ad,
        'form': form
        }
    return render(request,'new/index.html',context = context)

def news_info(request,pk):
    news_search = news.objects.filter(pk = pk)

    context={
        "ad":news_search,
        }

    return render(request,"new/news.html",context = context)
