from django.contrib.auth import views as views_auth
from django.urls import path, re_path, include
from . import views
from .forms import LoginForm

urlpatterns = [
    path('contact/', views.contact),
    path('logout/', views.logout_user, name='logout'),
    # path('signup/', views.signup, name='signup'),
    path('client/info/', include('client.urls'), name='info_client'),
    path('client/', include('client.urls'), name='register_client'),
    path('doctor/', include('doctor.urls'), name='signup'),
    path('login/', views_auth.LoginView.as_view(template_name='hospital/login.html', authentication_form=LoginForm), name='login'),
    path('info/', views.info, name='info'),
    # re_path(r'^info', include('service.urls')),
    path('', views.index),
]

