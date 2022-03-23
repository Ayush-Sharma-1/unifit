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
    universities = University.objects.all().order_by('UniRank')
    countrylist=University.objects.all().values_list('Country', flat=True).distinct()
    departmentlist=University_Department.objects.all().values_list('DeptName', flat=True).distinct()    
    if 'countrydropdown' in request.GET or 'departmentdropdown' in request.GET:
        countrydropdown = request.GET.get('countrydropdown')
        departmentdropdown = request.GET.get('departmentdropdown')
        UniNameList=University_Department.objects.filter(DeptName=departmentdropdown).values_list('UniName', flat=True)
        if countrydropdown!='all' and countrydropdown is not None:
            universities = universities.filter(Country=countrydropdown)
        if departmentdropdown!='all' and departmentdropdown is not None:
            universities = universities.filter(UniId__in=UniNameList)
    return render(request, 'uni_fit/home.html', {'universities': universities, 'countrylist':countrylist, 'departmentlist':departmentlist} )

def profile(request):
    return render(request, 'uni_fit/profile.html',)

@login_required
def favourite_add(request, id):
    university = get_object_or_404(University, UniId=id)
    if (university.FavouriteUnversity.filter(id=request.user.id).exists()):
        university.FavouriteUnversity.remove(request.user)
    else:
        university.FavouriteUnversity.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def favourite_list(request):
    fav_list = University.objects.filter(FavouriteUnversity=request.user.id)
    return render(request, 'uni_fit/favourites.html', {'fav_list': fav_list})

def university(request, id):
    result_list = []
    result_list = get_posts()
    #return render(request, 'uni_fit/university.html', {'result_list': result_list})

    #university data for the page
    unidata = University.objects.get(UniId=id)

#def post_detail(request):
    template_name = 'uni_fit/university.html'
    uni = get_object_or_404(Post)
    comments = uni.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.uni = uni
            # Save the comment to the database
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    
    return render(request, template_name, {'uni': uni,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'result_list': result_list,
                                           'unidata': unidata})

