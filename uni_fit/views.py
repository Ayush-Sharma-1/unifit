import re
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'uni_fit/index.html',)
