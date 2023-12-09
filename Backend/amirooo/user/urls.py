from django.contrib import admin
from django.urls import path, include
from user.views import *

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', singInSingUp, name='loginForm'),
    path('<str:username>/', UserProfile, name='profile')
]