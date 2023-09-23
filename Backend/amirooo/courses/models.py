from django.db import models
from tinymce.models import HTMLField
from user.models import User
from django.core.files.storage import FileSystemStorage

# Create your models here.
class Course(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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

    def __str__(self):
        return self.title
    
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

