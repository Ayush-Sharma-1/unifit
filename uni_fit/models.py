from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Users(models.Model):
    UserId = models.IntegerField
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    DepartmentPreference = models.CharField(max_length=100)
    SubjectPreference = models.CharField(max_length=100)
    Grade = models.IntegerField
    

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.UserId

class University(models.Model):
    UniId = models.AutoField(primary_key=True, auto_created=True)
    UniName = models.CharField(max_length=100, unique=True, default='TestName')
    Country = models.CharField(max_length=100)
    UniRank = models.IntegerField(default=0)
    About = models.CharField(max_length=500)
    Link = models.CharField(max_length=30)
    FavouriteUnversity = models.ManyToManyField(User,related_name='favourite',default=None, blank=True)

    class Meta:
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.UniName

class University_Department(models.Model):
    DeptId = models.AutoField(primary_key=True, auto_created=True)
    UniName = models.ForeignKey(University, on_delete=models.CASCADE, default=0)
    DeptName = models.CharField(max_length=100)
    DeptRank = models.IntegerField(default=0)
    Link = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "University_Departments"    

    def __str__(self):
        return self.DeptName    

class Review(models.Model):
    UniId = models.IntegerField
    Title = models.CharField(max_length=300)
    Comment = models.CharField(max_length=300)
    StudentSatisfaction = models.IntegerField
    EntryStandards = models.IntegerField
    GraduateProspect = models.IntegerField  

    class Meta:
        verbose_name_plural = "Reviews"     

    def __str__(self):
        return self.UniId


class Reddit(models.Model):
    UniName  = models.ForeignKey(University, on_delete=models.CASCADE)
    SubReddit = models.CharField(max_length=100)
    Link = models.CharField(max_length=500) 

    class Meta:
        verbose_name_plural = "Reddits"     

    def __str__(self):
        return self.UniName 

# this is just an extra model i used to create comments for, the comment model refers to this
# but for the final code we would need to use the University model rather than
# the Post model
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    uni = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    title = models.CharField(max_length=80)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.title)
