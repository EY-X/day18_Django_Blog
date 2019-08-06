from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import * 

def home_page(request):
    articles = Article.objects.order_by('-published_date')
    context = {
        'current_time': datetime.now(),
        'articles': articles
    }

    response = render(request, 'index.html', context)
    return HttpResponse(response)

def root(request):
    return HttpResponseRedirect('home')

def article_show(request, id):
    article = Article.objects.get(pk=id)
    context = {'article': article}

    response = render(request, 'article.html', context)
    return HttpResponse(response)