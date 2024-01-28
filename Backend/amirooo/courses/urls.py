from django.contrib import admin
from django.urls import path, include
from courses.views import *

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('hackmirooo/', MainCoursesH, name='MainCourses'),
    path('programmirooo/', MainCoursesP, name='MainCourses'),
    path('<str:name>/', CourseDitails, name='CoursesDetails'),
    path("add_to_cart/<str:name>", add_to_cart, name="add_to_cart"),
    path('remove_item/<str:name>', remove_item, name="remove_item"),
]
