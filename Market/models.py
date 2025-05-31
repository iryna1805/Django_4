from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthday = models.DateField()
    age = models.IntegerField()
    mail = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Musician(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_name} - {self.quantity}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class FeaturedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Featured: {self.product.name}"


class TopProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Top: {self.product.name}"


class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
