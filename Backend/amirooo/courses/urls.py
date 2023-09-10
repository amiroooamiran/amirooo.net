from django.contrib import admin
from django.urls import path, include
from courses.views import *

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', MainCourses, name='MainCourses')
]
