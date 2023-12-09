from django.contrib import admin
from django.urls import path, include
from courses.views import *

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', MainCourses, name='MainCourses'),
    path('Courses/<str:name>', CourseDitails, name='CoursesDetails'),
    path("add_to_cart/<str:name>", add_to_cart, name="add_to_cart"),
]
