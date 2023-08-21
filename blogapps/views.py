from django.shortcuts import render, redirect
from django.http import HttpResponse
from blogapps.models import UserPost
from .forms import UserPostForm

# Create your views here.
def index(request):
    post_data = UserPost.objects.all()
    return render(request, 'index.html' , {'post_data': post_data})

def show_post(request, post_id):
    post_data = UserPost.objects.get(id=post_id)
    if request.method == 'POST':
        post_data.delete()
        return redirect('blog')
    else:
        return render(request, 'post.html', {'post_data': post_data})
    

def create_post(request):
    post_form = UserPostForm()
    if request.method == 'POST':
        post_form = UserPostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('blog')
        else:
            return HttpResponse("Error Create Post")

    dict_form = {'post_form': post_form}
    return render(request, 'add_post.html', dict_form)

def edit_post(request, post_id):
    post_data = UserPost.objects.get(id=post_id)
    post_form = UserPostForm(instance=post_data)
    if request.method == 'POST':
        post_form = UserPostForm(request.POST, instance=post_data)
        if post_form.is_valid():
            post_form.save()
            return redirect('blog')
        else:
            return HttpResponse("Error Update Post")

    dict_form = {'post_form': post_form}
    return render(request, 'add_post.html', dict_form)