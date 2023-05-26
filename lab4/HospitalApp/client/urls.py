from django.urls import path
from . import views


urlpatterns = [
    path('', views.register_client, name='signup'),
    path('info/', views.info, name='info_client'),
    path('order/', views.order, name='order'),
    path('order/complete', views.finish_order, name='finish_order'),
]