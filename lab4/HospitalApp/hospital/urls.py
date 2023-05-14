from django.contrib.auth import views as views_auth
from django.urls import path, re_path, include
from . import views
from .forms import LoginForm

app_name = 'hospital'

urlpatterns = [
    path('contact/', views.contact),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('register_client/', include('client.urls'), name='register_client'),
    path('register_doctor/', include('doctor.urls'), name='register_doctor'),
    path('login/', views_auth.LoginView.as_view(template_name='hospital/login.html', authentication_form=LoginForm), name='login'),
    re_path(r'^info', include('service.urls')),
    path('', views.index),
]

