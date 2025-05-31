from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('register/', views.register, name='register'),
    path('admin_register/', views.admin_register, name='admin_register'),
    path('login/', views.login_view, name='login'),

    path('add_product/', views.add_product, name='add_product'),

    path('admin_lists/', views.admin_lists, name='admin_lists'),

    path('logout/', auth_views.LogoutView.as_view(template_name='Market/logout.html'), name='logout'),
]

