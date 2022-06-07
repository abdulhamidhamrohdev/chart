import imp
from turtle import home
from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path('exsamp/', example)
]
