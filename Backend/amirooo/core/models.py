from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# create a last updates
class Updates(models.Model):
    title = models.CharField(max_length=500, null=False)
    message = HTMLField(blank=True)
    previev = models.ImageField(upload_to='updates/', blank=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    
# create my last activate in any ware and showing last 1