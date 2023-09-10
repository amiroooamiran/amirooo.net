from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class User (models.Model):
    Profile = models.ImageField(upload_to="profiles", default="defultProfile.jpg")
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Fullname = models.CharField(max_length=250, blank=True)
    Nikname = models.CharField(max_length=100, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    Email = models.EmailField(max_length=254, blank=True)

    def __str__(self):
        return self.User.username
