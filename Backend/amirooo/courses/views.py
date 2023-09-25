from django.shortcuts import render
from courses.models import *
from user.models import User as us
# Create your views here.

def MainCourses(request):
    courses = Course.objects.all()
    tags = Tag.objects.all()

    if request.user.is_authenticated:
        # Get a single user profile object that matches the logged-in user
        user_profile = us.objects.get(user=request.user)
    else:
        # Do something else for anonymous users, such as showing a default profile or a message
        user_profile = None

    context ={
        'courses' : courses,
        'tags' : tags,
        'user_profile' : user_profile
    }
    return render(request, 'course/MainCourse.html', context)

def CourseDitails(request, name):
    course = Course.objects.get(name=name)
    chapter = Chapter.objects.all()
    video = Video.objects.all()

    context={
        'course' : course,
        'chapter' : chapter,
        'video' : video,
    }
    return render(request, 'course/CoursesDetails.html', context)