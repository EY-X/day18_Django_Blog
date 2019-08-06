from django.urls import path
from blog.views import *
from django.contrib import admin


urlpatterns = [
    path('home/', home_page),
    path('', root),
    path('admin/', admin.site.urls),
    path('articles/<int:id>', article_show, name='article_page'),
    path('article/new', new),
    path('article/create', article_create, name='article_create'),
    
]
