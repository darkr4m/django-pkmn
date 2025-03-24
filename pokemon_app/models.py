from django.db import models
from django.utils import timezone

# Create your models here.

# models.Model tell Django this is a Model that should be reflected on our database
class Pokemon(models.Model):
    # CharField is a character field and has a default max length of 255 characters
    name = models.CharField(max_length=255)
    # IntegerField will allow only solid numerical values as input
    level = models.IntegerField(default=1)
    date_encountered = models.DateField(default="2025-01-01")
    date_captured = models.DateTimeField(default=timezone.now)
    description = models.TextField(default="Unknown")
    captured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {'has been captured.' if self.captured else 'has yet to be caught.'}"
    
    def level_up(self):
        self.level += 1
        self.save()

    def change_caught_status(self):
        self.captured = not self.captured
        self.save()

#TERMINAL
#python manage.py makemigrations
# python manage.py migrate