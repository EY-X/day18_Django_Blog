from django.urls import path
from blog.views import *
from django.contrib import admin


urlpatterns = [
    path('home/', home_page),
    path('admin/', admin.site.urls),
    path('articles/<int:id>', article_show, name='article_page'),
]
