from django.urls import path 
from . import views

app_name = "nariz_electronica"
urlpatterns = [
    path("index", views.index, name="index-nariz"),
]
