from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')

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
            messages.error(request, "Username or Password is incorrect.")

    return render(request, 'login_user.html')

def user_register(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occurred during registration.")
    register_dict = {'page': page, 'form': form}
    return render(request, 'login_user.html', register_dict)


def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def user_home(request):
    return render(request, 'home_user.html')

