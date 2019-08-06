from django.forms import ModelForm
from blog.models import *


class ArticleForm(ModelForm):
    class Meta: 
        model = Article
        fields = ['title', 'body', 'author']