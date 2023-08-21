from django.shortcuts import render
from django.http import HttpResponse
from blogapps.models import UserPost
from .forms import UserPostForm

# Create your views here.
def index(request):
    post_data = UserPost.objects.all()
    return render(request, 'index.html' , {'post_data': post_data})

def show_post(request, post_id):
    post_data = UserPost.objects.get(id=post_id)
    return render(request, 'post.html', {'post_data': post_data})

def create_post(request):
    post_form = UserPostForm()
    dict_form = {'post_form': post_form}
    return render(request, 'add_post.html', dict_form)