from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from courses.models import *
from user.models import User as us

from django.contrib import messages

from django.utils import timezone
# Create your views here.

def MainCoursesH(request):
    courses = Course.objects.all()
    tags = Tag.objects.all()

    if request.user.is_authenticated:
        # Get a single user profile object that matches the logged-in user
        user_profile = us.objects.get(user=request.user)
    else:
        # Do something else for anonymous users, such as showing a default profile or a message
        user_profile = None

    context ={
        'courses' : courses,
        'tags' : tags,
        'user_profile' : user_profile
    }
    return render(request, 'course/CoursesH-main.html', context)


def MainCoursesP(request):
    courses = Course.objects.all()
    tags = Tag.objects.all()

    if request.user.is_authenticated:
        # Get a single user profile object that matches the logged-in user
        user_profile = us.objects.get(user=request.user)
    else:
        # Do something else for anonymous users, such as showing a default profile or a message
        user_profile = None

    context ={
        'courses' : courses,
        'tags' : tags,
        'user_profile' : user_profile
    }
    return render(request, 'course/CoursesP-main.html', context)

def CourseDitails(request, name):
    course = Course.objects.get(name=name)
    chapter = Chapter.objects.all()
    video = Video.objects.all()

    if request.user.is_authenticated:
        # Get a single user profile object that matches the logged-in user
        user_profile = us.objects.get(user=request.user)
    else:
        # Do something else for anonymous users, such as showing a default profile or a message
        user_profile = None

    context={
        'course' : course,
        'chapter' : chapter,
        'video' : video,
        'user_profile' : user_profile
    }
    return render(request, 'course/CoursesDetails.html', context)

def add_to_cart(request, name):
    course = Course.objects.get(name=name)

    order_item, created = OrderItem.objects.get_or_create(
        course = course,
        user = request.user,
        ordered = False,
    )

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(course__name = name).exists():
            order_item.save()
            messages.info(request, ".این دوره قبلا اضافه شده است")
            return redirect("CoursesDetails", name=name)
        else:
            order.items.add(order_item)
            messages.info(request, "این دوره در سبد خرید شما اضافه شد")
            return redirect("CoursesDetails", name=name)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user = request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "این دوره در سبد خرید شما اضافه شد")
        return redirect("CoursesDetails", name=name)


def remove_item(request, name):
    # Get the product based on name
    course = get_object_or_404(Course, name=name)

    # Check if there's an open order for the user
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs.first()

        # Check if the product is in the order
        if order.items.filter(course=course).exists():
            # Remove the OrderItem for the product from the order
            order_item = order.items.filter(course=course, user=request.user, ordered=False).first()
            order_item.delete()

            messages.info(request, "The product has been removed")
        else:
            messages.info(request, "This product is not in your shopping cart")
    else:
        messages.info(request, "You have not customized any records")

    return redirect("carts", username=request.user.username)