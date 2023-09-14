from django.contrib.auth import views as views_auth
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.reviews, name="reviews"),
    path('add/', views.add_review, name="add_review")
]
