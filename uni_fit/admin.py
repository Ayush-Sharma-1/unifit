from django.contrib import admin
from uni_fit.models import UserProfile,InternalData, Review, University, University_Department, Users

admin.site.register(UserProfile)
admin.site.register(Users)
admin.site.register(University)
admin.site.register(University_Department)
admin.site.register(Review)
admin.site.register(InternalData)
