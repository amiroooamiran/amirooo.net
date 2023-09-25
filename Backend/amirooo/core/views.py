from django.shortcuts import render
from user.models import User as us
# Create your views here.

def Index(request):

    if request.user.is_authenticated:
        # Get a single user profile object that matches the logged-in user
        user_profile = us.objects.get(user=request.user)
    else:
        # Do something else for anonymous users, such as showing a default profile or a message
        user_profile = None

    context = {
        'user_profile' : user_profile
    }
    return render(request, 'Index/Index.html', context)


def about(request):
    return render(request, 'Index/about.html')

def contact(request):
    return render(request, 'Index/contact.html')