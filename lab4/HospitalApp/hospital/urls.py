from django.contrib.auth import views as views_auth
from django.urls import path, re_path, include
from . import views
from .forms import LoginForm
urlpatterns = [
    path('contact/', views.contact),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('register_client/', views.register_client, name='register_client'),
    path('register_doctor/', views.register_doctor, name='register_doctor'),
    path('login/', views.login, name='login'),
    re_path(r'^info', include('service.urls')),
    path('', views.index),
]

