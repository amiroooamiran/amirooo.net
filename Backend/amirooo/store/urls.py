from django.urls import path, include
from .views import *

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', store, name="store"),
    path('product/', product, name="product")    
]
