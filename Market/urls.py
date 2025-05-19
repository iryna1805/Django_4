from django.urls import path
from . import views
from .views import register, admin_register, login_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', register, name='register'),
    path('admin_register/', admin_register, name='admin_register'),
    path('login/', login_view, name='login'),
]
