from django.contrib.auth import views as views_auth
from django.urls import path, include
from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('signup/', views.signup, name='signup'),
    path('login/', views_auth.LoginView.as_view(template_name='hospital/login.html', authentication_form=LoginForm),
         name='login'),
    path('info/', include('service.urls')),
]
