from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Make(models.Model):
    make = models.CharField('Make', max_length=150)


class CarModel(models.Model):
    make = models.ForeignKey(Make, on_delete = models.CASCADE, related_name='models')
    model = models.CharField('Model', max_length=150)


class CarListing(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    make_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    registration_plate = models.CharField(max_length=10)
    mileage = models.IntegerField()
    fuel = models.IntegerField(
        validators = [
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    rent_count = models.IntegerField()
    is_rented = models.BooleanField()
    basic_price = models.FloatField()
    production_year = models.IntegerField()


class Client(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length = 254)
    phone_number = models.CharField(max_length = 15)
    rented_cars_number = models.IntegerField()
    balance = models.FloatField()
    money_spent = models.FloatField()


class Employee(models.Model):
    first_name: models.CharField(max_length = 60)
    last_name: models.CharField(max_length = 60)
    email: models.EmailField(max_length = 254)
    password: models.CharField(max_length = 254)
    phone_number: models.CharField(max_length = 15)


class Rentals(models.Model):
    rent_client: models.ForeignKey(Client, on_delete = models.SET_NULL)
    rent_employee: models.ForeignKey(Employee, on_delete = models.SET_NULL)
    car_info: models.ForeignKey(CarListing, on_delete = models.SET_NULL)
    price: models.FloatField()
    rent_start: models.DateField()
    rent_end: models.DateField()
    is_active: models.BooleanField()

