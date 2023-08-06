from django.contrib import admin
from user.models import *
# Register your models here.

class UserSInfo(admin.ModelAdmin):
    user_options = ("UserName", "Fname", "Lname" "Phone_number")

admin.site.register(User, UserSInfo)