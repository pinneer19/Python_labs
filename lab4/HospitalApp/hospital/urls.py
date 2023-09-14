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
    path('login/', views_auth.LoginView.as_view(template_name='hospital/login.html', authentication_form=LoginForm),
         name='login'),
    path('info/', views.info, name='info'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('coupons/', views.coupons, name='coupons'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('jobs/', views.jobs, name='jobs'),
    path('news/', views.news, name='news'),
    path('privacy/', views.privacy, name='privacy'),
    path('reviews/', include('review.urls'), name='reviews'),
    path('main/', views.main, name='superuser'),
    path('statistics/', views.statistics, name='statistics'),
    path('add/<str:item_type>/', views.add_item, name='add_item'),
    path('add/order/services/', views.add_services_to_order, name='add_services'),
    path('delete/<str:item_type>/<int:item_id>/', views.delete_item, name='delete_item'),
    path('edit/<str:item_type>/<int:item_id1>/<int:item_id2>/', views.edit_item, name='edit_item'),
    path('', views.index),
    path('<path:unknown>', views.unknown_page, name='unknown_page'),
]
