from django.contrib.auth import views as views_auth
from django.urls import path, re_path, include
from . import views
from .forms import LoginForm

urlpatterns = [
    path('contact/', views.contact),
    path('logout/', views.logout_user, name='logout'),
    # path('client/info/', include('client.urls'), name='info_client'),
    path('client/', include('client.urls'), name='signup'),
    path('doctor/', include('doctor.urls'), name='info_doctor'),
    path('login/', views_auth.LoginView.as_view(template_name='hospital/login.html', authentication_form=LoginForm), name='login'),
    path('info/', views.info, name='info'),
    path('main/', views.main, name='superuser'),
    path('add/<str:item_type>/', views.add_item, name='add_item'),
    path('add/order/services/', views.add_services_to_order, name='add_services'),
    path('delete/<str:item_type>/<int:item_id>/', views.delete_item, name='delete_item'),
    path('edit/<str:item_type>/<int:item_id1>/<int:item_id2>/', views.edit_item, name='edit_item'),
    # re_path(r'^info', include('service.urls')),
    path('', views.index),
]

