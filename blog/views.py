from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        'current_time':datetime.now()
    }

    response = render(request, 'index.html', context)
    return HttpResponse(response)