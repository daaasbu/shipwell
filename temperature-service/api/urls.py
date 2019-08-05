from django.contrib import admin
from django.urls import path
from .averages_view import get_average_temp
urlpatterns = [
    path('temp', get_average_temp, name='get_average_temp')
]
