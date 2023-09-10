from django.shortcuts import render, redirect

# Create your views here.
def singInSingUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)
    
    return render(request, 'user/SingInSingUp.html')