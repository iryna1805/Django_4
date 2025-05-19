from django.shortcuts import render, redirect
from .models import Musician, Album
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, AdminRegisterForm

def home(request):
    musicians = Musician.objects.all()
    albums = Album.objects.all()
    return render(request, 'Market/index.html', {'musicians': musicians, 'albums': albums})

def about(request):
    return render(request, 'Market/about_me.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'Market/register.html', {'form': form})


def admin_register(request):
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = AdminRegisterForm()
    return render(request, 'Market/admin_register.html', {'form': form})


def login_view(request):
    return render(request, 'Market/login.html')
