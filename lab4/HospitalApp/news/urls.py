from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.news,name='news'),
    path('<int:news_id>/', views.news_info,  name='news_info')
]
