from django.urls import path
from . import views

urlpatterns= [
    path("", views.index, name='index'),
    path("anand", views.anand, name='anand'),
    path("<str:name>", views.greet, name= "greet")


] 