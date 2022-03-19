from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from uni_fit.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import profile
from stat import FILE_ATTRIBUTE_SPARSE_FILE
from uni_fit.reddit import get_posts
from uni_fit.models import University, Users

def index(request):
    return render(request, 'uni_fit/index.html',)

def home(request):
    context_dict = {}
    university_list = University.objects.all().order_by('UniRank')
    context_dict['universities'] = university_list
    return render(request, 'uni_fit/home.html', context=context_dict)

def profile(request):
    return render(request, 'uni_fit/profile.html',)

@login_required
def favourite_add(request, id):
    university = get_object_or_404(University, UniId=id)
    if (university.FavouriteUnversity.filter(UserId=request.Users.UserId).exists()):
        university.FavouriteUnversity.remove(request.Users)
    else:
        university.FavouriteUnversity.add(request.Users)
    return(request, 'uni_fit/home.html')

@login_required
def favourite_list(request):
    l = University.FavouriteUnversity.get(University.FavouriteUnversity)
    fav_list = University.FavouriteUnversity.filter(l=request.Users)
    return(request, 'uni_fit/favourites.html', {'fav_list': fav_list})

def reddit(request):
    result_list = []
    result_list = get_posts()
    return render(request, 'uni_fit/university.html', {'result_list': result_list})