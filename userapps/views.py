from django.shortcuts import render, redirect
from django.http import HttpResponse

def user_login(request):
    return render(request, 'login_user.html')

# Create your views here.
