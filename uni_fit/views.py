from webbrowser import get
from django.urls import reverse
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from uni_fit.forms import UserForm, UserProfileForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import profile
from stat import FILE_ATTRIBUTE_SPARSE_FILE
from uni_fit.reddit import get_posts
from uni_fit.models import University, Users, Post, University_Department


def index(request):
    return render(request, 'uni_fit/index.html',)

@login_required
def home(request):
    context_dict = {}
    university_list = University.objects.all().order_by('UniRank')
    context_dict['universities'] = university_list
    countrylist=University.objects.all().values_list('Country', flat=True).distinct()
    departmentlist=University_Department.objects.all().values_list('DeptName', flat=True).distinct()
    return render(request, 'uni_fit/home.html', {'universities': university_list, 'countrylist':countrylist, 'departmentlist':departmentlist} )

def profile(request):
    return render(request, 'uni_fit/profile.html',)

@login_required
def favourite_add(request, id):
    university = get_object_or_404(University, FavouriteUnversity = id)
    if (university.FavouriteUnversity.filter(FavouriteUnversity=request.user.id).exists()):
        university.FavouriteUnversity.remove(request.user)
    else:
        university.FavouriteUnversity.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def favourite_list(request):
    fav_list = University.objects.filter(FavouriteUnversity=request.user.id)
    return render(request, 'uni_fit/favourites.html', {'fav_list': fav_list})

def reddit(request):
    result_list = []
    result_list = get_posts()
    return render(request, 'uni_fit/university.html', {'result_list': result_list})

def post_detail(request):
    template_name = 'uni_fit/review.html'
    post = get_object_or_404(Post)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
