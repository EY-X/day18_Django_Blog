from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import * 
from blog.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home')
            else:
                form.add_error('username', 'Login failed')
    else:
        form = LoginForm()

    return render(request, 'login.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/home')  


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/home')
    else:
        form = UserCreationForm()
    html_response =  render(request, 'signup.html', {'form': form})
    return HttpResponse(html_response)

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


def article_delete(request):
    form = ArticleForm(request.DELETE)

