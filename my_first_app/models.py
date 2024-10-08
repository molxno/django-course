from django.db import models


# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    price = models.IntegerField()
    type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.color} {self.price} {self.type}"


class Runner(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name} {self.age} {self.car}"


class Publisher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.birth_date}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return f"{self.title} {self.publisher} {self.authors}"
