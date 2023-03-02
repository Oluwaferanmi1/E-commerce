from django.urls import path
from . import views


#URLConfiguration
urlpatterns = [
    path('hello/', views.say_hello)

]


#this is where we map URL to views.py