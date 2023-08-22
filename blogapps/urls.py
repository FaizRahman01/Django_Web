from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.index, name='blog'),
    path('view/<str:post_id>', views.show_post, name='showpost'),
    path('create', views.create_post, name='createpost'),
    path('edit/<str:post_id>', views.edit_post, name='editpost'),
]