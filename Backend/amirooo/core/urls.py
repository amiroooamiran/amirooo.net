from django.contrib import admin
from django.urls import path, include
from core.views import *


urlpatterns = [
    path('', Index, name='Index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
<<<<<<< HEAD
    path('logout/', logout_view, name='logout'),

    path('tinymce/', include('tinymce.urls')),
=======
    path('logout/', logout_view, name='logout')
>>>>>>> 142e890c90a6b9db12ae3e641f3d195377e8b077
]
