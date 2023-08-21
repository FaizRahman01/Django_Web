from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('post/view/<str:post_id>', views.show_post, name='showpost'),
    path('post/create', views.create_post, name='createpost'),
    path('post/edit/<str:post_id>', views.edit_post, name='editpost'),
]