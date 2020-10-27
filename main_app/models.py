from django.db import models

# Create your models here.
COLORS = (
    ('Red','Red'),
    ('Blue','Blue'),
    ('Yellow','Yellow'),
    ('Purple','Purple'),
    ("Black","Black"),
    ('White','White'),
)
class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.CharField(
        max_length=10,
        choices=COLORS
    )
    price = models.IntegerField()

    def __str__(self):
        return self.name
