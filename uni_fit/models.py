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

class InternalData(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Internal Data"

    def __str__(self):
        return self.name


class Users(models.Model):
    internalData = models.ForeignKey(InternalData, on_delete=models.CASCADE)
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
        return self.text

class University(models.Model):
    internalData = models.ForeignKey(InternalData, on_delete=models.CASCADE)
    UniId = models.AutoField(primary_key=True, default=0)
    UniName = models.CharField(max_length=100, unique=True, default='TestName')
    Country = models.CharField(max_length=100)
    UniRank = models.IntegerField(default=0)
    About = models.CharField(max_length=500)
    Link = models.CharField(max_length=30)
    FavouriteUnversity = models.ManyToManyField(Users,related_name='favourite',default=None, blank=True)

    class Meta:
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.text

class University_Department(models.Model):
    internalData = models.ForeignKey(InternalData, on_delete=models.CASCADE)
    DeptId = models.AutoField(primary_key=True, default=0)
    UniId = models.ForeignKey(University, on_delete=models.CASCADE, default=0)
    DeptName = models.CharField(max_length=100)
    DeptRank = models.IntegerField
    About = models.CharField(max_length=30)
    Link = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "University_Departments"    

    def __str__(self):
        return self.text     

class Review(models.Model):
    internalData = models.ForeignKey(InternalData, on_delete=models.CASCADE)
    UniId = models.IntegerField
    Title = models.CharField(max_length=300)
    Comment = models.CharField(max_length=300)
    StudentSatisfaction = models.IntegerField
    EntryStandards = models.IntegerField
    GraduateProspect = models.IntegerField  

    class Meta:
        verbose_name_plural = "Reviews"     

    def __str__(self):
        return self.text 