from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info, name='info_doctor'),
    # path('', views.info, name='info_doctor'),
]
