from django.shortcuts import render, redirect
from .models import Musician, Album
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, AdminRegisterForm
from django.core.paginator import Paginator


def home(request):
    musicians_list = Musician.objects.all()
    albums_list = Album.objects.all()

    # Пагінація
    paginator_musicians = Paginator(musicians_list, 5)  
    page_number_musicians = request.GET.get('page_musicians')
    musicians = paginator_musicians.get_page(page_number_musicians)

    # Пагінація
    paginator_albums = Paginator(albums_list, 5)
    page_number_albums = request.GET.get('page_albums')
    albums = paginator_albums.get_page(page_number_albums)

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
