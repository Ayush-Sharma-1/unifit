from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from uni_fit.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import profile
from stat import FILE_ATTRIBUTE_SPARSE_FILE

def index(request):
    return render(request, 'uni_fit/index.html',)

def home(request):
    return render(request, 'uni_fit/home.html',)

def profile(request):
    return render(request, 'uni_fit/profile.html',)