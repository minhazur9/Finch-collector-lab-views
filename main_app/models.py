from django.db import models
from django.contrib.auth.models import User

# Create your models here.
COLORS = (
    ('Red', 'Red'),
    ('Blue', 'Blue'),
    ('Yellow', 'Yellow'),
    ('Purple', 'Purple'),
    ("Black", "Black"),
    ('White', 'White'),
)

BRANDS = (
    ("Audi", "Audi"),
    ("BMW", "BMW"),
    ("Citroen", "Citroen"),
    ("Ford", "Ford"),
    ("Honda", "Honda"),
    ("Jaguar", "Jaguar"),
    ("Land Rover", "Land Rover"),
    ("Mercedes", "Mercedes"),
    ("Mini", "Mini"),
    ("Nissan", "Nissan"),
    ("Toyota", "Toyota"),
    ("Volvo", "Volvo"),
    ("Tesla", "Tesla"),
)

CAR_UPGRADES = (
    ('Wider Tires', 'Wider Tires'),
    ('High-Performance Coils', 'High-Performance Coils'),
    ('Larger Anti-Roll Bars', 'Larger Anti-Roll Bars'),
    ('Chassis Braces', 'Chassis Braces'),
    ('Larger Diameter Catalyst-Back Exhaust',
     'Larger Diameter Catalyst-Back Exhaust'),
    ('Stiffer Motor Mounts', 'Stiffer Motor Mounts'),
    ('Performance Seats', 'Performance Seats'),
    ('High-Temperature Brake Pads', 'High-Temperature Brake Pads'),
    ('Less Restrictive Cold-Air Intake', 'Less Restrictive Cold-Air Intake'),
    ('Stainless-Steel Braided Brake Lines', 'Stainless-Steel Braided Brake Lines'),
)


class Extra(models.Model):
    name = models.CharField(
        max_length=100
    )
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(
        max_length=20,
        choices=BRANDS,
    )
    color = models.CharField(
        max_length=10,
        choices=COLORS
    )
    price = models.IntegerField()
    extras = models.ManyToManyField(
        Extra,
        blank=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Upgrade(models.Model):
    name = models.CharField(
        max_length=100,
        choices=CAR_UPGRADES
    )
    price = models.IntegerField()

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
