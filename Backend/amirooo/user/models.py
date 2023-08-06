from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class User (models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    Email = models.EmailField(max_length=254, blank=True)

    def __str__(self):
        return self.User.username
