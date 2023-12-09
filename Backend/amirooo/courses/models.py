from django.db import models
from tinymce.models import HTMLField
from django.core.validators import RegexValidator
from user.models import User
from django.core.files.storage import FileSystemStorage
import uuid

class Teacher(models.Model):
    Profile = models.ImageField(upload_to="profiles", default="defultProfile.jpg")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Bio = HTMLField(blank=True)
    teacher = models.BooleanField(default=False)
    Fullname = models.CharField(max_length=250, blank=True)
    Nikname = models.CharField(max_length=100, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    Email = models.EmailField(max_length=254, blank=True)

    def __str__(self):
        return self.user.username

# Create your models here.
class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length= 150, null=True)
    name = models.CharField(max_length= 150, null=True)
    banner = models.ImageField(upload_to='course/', blank=True)
    description = HTMLField(null=True)
    price = models.IntegerField(default=0.0, null=False)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default=False)
    Bought = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    length = models.IntegerField(null=False)
    likes = models.ManyToManyField(User, related_name='Likes', blank=True)
    Star = models.ManyToManyField(User, related_name='Star', blank=True)

    def get_add_to_cart(self):
        return reversed("courses:add-to-cart", kwargs={
            "pk" : self.title
        })
    
    def discount_price(self):
        descount = 100 - self.discount
        f_price = self.price * (descount / 100)
        return f_price

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def fina_price(self):
        price = self.course.price
        return price
    
    def final_discount(self):
        discount = self.course.discount_price
        return discount

    def __str__(self):
        return f'{self.user.username} {self.course.title}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    order_id = models.CharField(max_length=100, unique=True, default=None, blank=True, null=True)
    datetime_ofpayment = models.DateTimeField(auto_now_add=True)
    order_delivered = models.BooleanField(default=False)
    order_receved = models.BooleanField(default=False)

    razorpay_order_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_pyment_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=500, null=True, blank=True)

    order_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)

    def save(self,*args, **kwargs):
        if self.order_id is None and self.datetime_ofpayment and self.id:
            self.order_id = self.datetime_ofpayment.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        
        return super().save(*args, **kwargs)
        
    
    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.fina_price()
        return total
    
    def get_total_descount(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.final_discount()
        return total
    
    def __str__(self):
        return self.user.username

# main models of Courses 
class CourseProperty(models.Model):
    description = models.CharField(max_length=20, null=False,)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)

class Tag(CourseProperty):
    pass

class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass

# chapters Video
class Chapter(models.Model):
    course_id = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    chapter_id = models.IntegerField(null=False, default=0)
    title = models.CharField(max_length=300)
    videos_lenth = models.IntegerField(default=0, null=False)
    def __str__(self):
        return self.title

# Courses Video Model
class Video(models.Model):
    title = models.CharField(max_length=100, null=False)
    chapter = models.ForeignKey(Chapter, null=False, on_delete=models.CASCADE)
    serial_number = models.IntegerField()
    resource = models.FileField(upload_to="course/resource", blank=True)
    video_file = models.FileField(upload_to=f'course/video')
    is_prwview = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

