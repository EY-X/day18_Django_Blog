from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import * 
from blog.forms import *

def home_page(request):
    return render(request, 'index.html', {
        'current_time': datetime.now(),
        'articles': Article.objects.order_by('-published_date')
    })

def root(request):
    return HttpResponseRedirect('home')

def article_show(request, id):
    return render(request, 'article.html', {
        'article': Article.objects.get(pk=id)
    })

def new(request):
    return render(request, 'article-form.html',{
        'form': ArticleForm(),
        'message': 'Create an Article!',
        'action': '/article/create'
    })

def article_create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect('/home')

