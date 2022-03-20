from dataclasses import field
from django import forms
from uni_fit.models import UserProfile, Comment
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website','picture',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'comment')