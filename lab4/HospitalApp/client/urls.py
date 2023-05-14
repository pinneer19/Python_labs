from django.urls import path
from . import views


urlpatterns = [
    path('', views.register_client, name='register_client'),
]

