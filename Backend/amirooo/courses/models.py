from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length= 30, null=True)
    description = HTMLField(null=True)
    price = models.IntegerField(default=0.0, null=False)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to="course/resource")
    length = models.IntegerField(null=False)

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

# Courses Video Model
class Video(models.Model):
    title = models.CharField(max_length=100, null=False)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    serial_number = models.IntegerField()
    video_file = models.FileField(upload_to="course/videos")
    is_prwview = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title