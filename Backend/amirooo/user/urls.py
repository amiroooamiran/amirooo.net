from django.contrib import admin
from django.urls import path
from user.views import *

urlpatterns = [
    path('', singInSingUp, name='loginForm')
]