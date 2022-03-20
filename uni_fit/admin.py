from django.contrib import admin
from uni_fit.models import UserProfile,InternalData, Review, University, University_Department, Users, Post, Comment

admin.site.register(UserProfile)
admin.site.register(Users)
admin.site.register(University)
admin.site.register(University_Department)
admin.site.register(Review)
admin.site.register(InternalData)
admin.site.register(Post)
admin.site.register(Comment)
