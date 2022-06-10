from django.urls import path
from django.urls import path, include, re_path
from . import views





app_name = 'questionapp'





urlpatterns = [
    path('', views.index, name ='indexpage')
    ]