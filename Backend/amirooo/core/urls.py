from django.contrib import admin
from django.urls import path, include
from core.views import *


urlpatterns = [
    path('', Index, name='Index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('logout/', logout_view, name='logout'),

    path('tinymce/', include('tinymce.urls')),

    # order Segment
    path('Succes_payment', succes_payment, name="succesful_payment"),
    path('UnSucces_payment', un_succes_payment, name="UnSuccesful_payment")
]
