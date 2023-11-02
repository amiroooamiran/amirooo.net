from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from user.models import User as us
from courses.models import Course

# filtering strings with regex
import re
# Create your views here.
def singInSingUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        username_up = request.POST.get('username_up')
        password_up = request.POST.get('password_up')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        
        else:
            try:

                if User.objects.filter(username=username_up).exists():
                    messages.info(request, ".نام کاربری قبلا ثبت شده")
                    return redirect('loginForm')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, ".این ایمل قبلا یافت شده")
                    return redirect('loginForm')
                else:
                    user = User.objects.create_user(username_up, email, password_up)
                    user.save()

                    our_user = authenticate(username=username_up, password=password_up)

                    if our_user is not None:
                        login(request, user)
                        new_profile = us.objects.create(user=user)
                        new_profile.save()
                        messages.success(request, ".ثبت نام با موفقیت انجام شد")
                        return redirect('/')
                       
                    return redirect('loginForm')
            except:
                if user is None:
                    messages.info(request, ".نام کاربری یا رمز عبور اشتباه است")
    
        
    return render(request, 'user/SingInSingUp.html')

def UserProfile(request, username):
    user = User.objects.get(username=username)

    if request.user.is_authenticated:
        # Get a single user profile object that matches the logged-in user
        user_profile = us.objects.get(user=request.user)
    else:
        # Do something else for anonymous users, such as showing a default profile or a message
        user_profile = None
        url_name = request.path #filtering path with regex.

    
    course_ditails = Course.objects.all()

    context ={
        'user' : user,
        'user_profile' : user_profile,
        'course_ditails' : course_ditails,
    }
    return render(request, 'user/UserProfile.html', context)