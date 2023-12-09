from django.shortcuts import render, redirect

# importing Models from other applications
from user.models import User as us
from courses.models import *
from core.models import *

from django.contrib.auth import logout
# Create your views here.

def Index(request):

    if request.user.is_authenticated:
        # Get a single user profile object that matches the logged-in user
        user_profile = us.objects.get(user=request.user)
    else:
        # Do something else for anonymous users, such as showing a default profile or a message
        user_profile = None
    
    # courses Models
    courses = Course.objects.all()
    tags = Tag.objects.all()
    techers = us.objects.all()

    updates = Updates.objects.all()

    context = {
        'user_profile' : user_profile,
        'courses' : courses,
        'tags' : tags,
        'techers': techers,
        'updates': updates
    }
    return render(request, 'Index/Index.html', context)


def about(request):
    return render(request, 'Index/about.html')

def contact(request):
    return render(request, 'Index/contact.html')

def logout_view(request):
    logout(request)
    return redirect('/')