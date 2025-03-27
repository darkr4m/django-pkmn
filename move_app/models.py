from django.db import models
from django.core import validators as v

# Create your models here.
class Move(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False, validators=[])
    accuracy = models.PositiveIntegerField(default=70, validators=[v.MinValueValidator(1), v.MaxValueValidator(100)])
    pp = models.PositiveIntegerField(default=20, validators=[v.MinValueValidator(1), v.MaxValueValidator(30)])
    power = models.PositiveIntegerField(default=80, validators=[v.MaxValueValidator(120)])

    def __str__(self):
        return f"| {self.name} | accuracy: {self.accuracy} | power: {self.power} | PP: {self.pp}"