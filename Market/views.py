from django.shortcuts import render, redirect
from .models import FeaturedProduct, TopProduct, Product
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, AdminRegisterForm, ProductForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test


from django.http import HttpResponse

def set_cookie_view(request):
    response = HttpResponse("Cookie встановлено!")
    # name = значення, max_age = час життя в секундах
    response.set_cookie("username", "iraba", max_age=3600)  # 1година
    return response

def get_cookie_view(request):
    username = request.COOKIES.get("username", "Гість")
    return HttpResponse(f"Привіт, {username}!")

def delete_cookie_view(request):
    response = HttpResponse("Cookie видалено!")
    response.delete_cookie("username")
    return response
#
def is_admin(user):
    return user.is_staff

from django.core.paginator import Paginator

def home(request):
    products_list = Product.objects.filter(available=True).order_by('-price')
    paginator = Paginator(products_list, 6)  # 6 продуктів на сторінці

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    featured = FeaturedProduct.objects.all()
    top = TopProduct.objects.all()

    featured_products = [fp.product for fp in featured]
    top_products = [tp.product for tp in top]

    context = {
        'products': products,
        'featured_products': featured_products,
        'top_products': top_products,
        'is_admin': request.user.is_staff,
    }
    return render(request, 'Market/index.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'Market/register.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'Market/add_product.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def admin_lists(request):
    featured = FeaturedProduct.objects.all()
    top = TopProduct.objects.all()
    context = {
        'featured': featured,
        'top': top,
    }
    return render(request, 'Market/admin_lists.html', context)


def about(request):
    return render(request, 'Market/about_me.html')

def login_view(request):
    return render(request, 'Market/login.html')

def admin_register(request):
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = AdminRegisterForm()
    return render(request, 'Market/admin_register.html', {'form': form})