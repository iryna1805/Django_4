from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)


    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'available']


class AdminRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    position = forms.CharField(max_length=50)


    class Meta:
        model = User
        fields = ['username', 'email', 'position', 'password1', 'password2']
