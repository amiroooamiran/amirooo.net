from django.shortcuts import render
from courses.models import *
# Create your views here.

def MainCourses(request):
    courses = Course.objects.all()
    tags = Tag.objects.all()

    context ={
        'courses' : courses,
        'tags' : tags
    }
    return render(request, 'course/Index_course.html', context)