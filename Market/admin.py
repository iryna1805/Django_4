from django.contrib import admin
from .models import Person, Musician, Album, Cart, Admin


admin.site.register(Person)

admin.site.register(Musician)

admin.site.register(Album)

admin.site.register(Cart)

admin.site.register(Admin)