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
admin.site.register(Teacher)

# Orders Category
class CourseOrderItem(admin.ModelAdmin):
    list_display = ("user", "course", "ordered")

class CourseOrder(admin.ModelAdmin):
    list_display = ("user", "start_date", "ordered_date", "ordered", "order_delivered", "razorpay_order_id")


admin.site.register(OrderItem, CourseOrderItem)
admin.site.register(Order, CourseOrder)

# Chapters and Video

class VideoInline(admin.TabularInline):
    model = Video

class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoInline]

admin.site.register(Chapter, VideoAdmin)