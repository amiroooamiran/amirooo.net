from django.contrib import admin
from courses.models import *
# Register your models here.

class TagAdmin(admin.TabularInline):
    model = Tag

class LearnAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

# addin all TabularInline Models in Course Models.

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, LearnAdmin, PrerequisiteAdmin]

admin.site.register(Course, CourseAdmin)