from django.urls import path
from . import views

urlpatterns = [
    path('', views. api_routes),
    path('posts/', views.get_posts),
    path('posts/<str:pk>/', views.get_post),
]

