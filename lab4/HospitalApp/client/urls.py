from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_client, name='register_client'),
    path('', views.info, name='info_client'),
]

