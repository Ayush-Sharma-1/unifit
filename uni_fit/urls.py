from django.urls import path
from uni_fit import views

app_name = 'uni_fit'

urlpatterns = [
    path('', views.index, name='index'),
]