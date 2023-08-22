from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def user_login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        try:
            user = User.objects.get(username=username)
        except:
            user = None
            print('User not found')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('username or password is incorrect')

    return render(request, 'login_user.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def user_home(request):
    return render(request, 'home_user.html')

