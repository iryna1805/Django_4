from django.shortcuts import render
from .models import Musician, Album


def home(request):
    musicians = Musician.objects.all()
    albums = Album.objects.all()
    return render(request, 'index.html', {'musicians': musicians, 'albums': albums})

def about(request):
    return render(request, 'about_me.html')



