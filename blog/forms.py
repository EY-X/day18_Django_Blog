from django.forms import ModelForm
from blog.models import *
from django.forms import CharField, PasswordInput, Form, ModelForm

class ArticleForm(ModelForm):
    class Meta: 
        model = Article
        fields = ['title', 'body', 'author']

class LoginForm(Form):
    username = CharField(label="User Name", max_length=64)
    password = CharField(widget=PasswordInput())