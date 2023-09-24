from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.db import IntegrityError

import re

from user.models import User as Us
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
                pattern = "^.*(?=.{6,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$"
                result = re.findall(pattern, password_up)

                if (result):
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
                            new_profile = Us.objects.create(user=user)
                            new_profile.save()
                            return redirect('/')
                        
                        messages.success(request, ".ثبت نام با موفقیت انجام شد")
                else:
                    messages.info(request, ".رمز عبور باید دارای 8 کارکتر و متشکل از حروف کوشک و بزرگ و یک علامت باشد")
                    return redirect('/')

                login(request, user) # log in the new user
                return redirect('/')
            except IntegrityError:
                messages.info(request, ".نام کاربری یا رمز عبور اشتباه است")
    
        
    return render(request, 'user/SingInSingUp.html')