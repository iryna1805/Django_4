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
