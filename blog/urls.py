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
    path('article/delete', article_delete, name='article_delete'),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('signup/', signup, name='signup'),

    
    
]
