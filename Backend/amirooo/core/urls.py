from django.contrib import admin
from django.urls import path, include
from core.views import *


urlpatterns = [
    path('', Index, name='Index'),
    path('about', about, name='about')
]
