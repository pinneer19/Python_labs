from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info, name='info_doctor'),
    path('complete/<int:item_id>', views.complete_service, name='complete_service'),
]
