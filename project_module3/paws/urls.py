from django.urls import path 
from . import views

app_name = "paws"
urlpatterns = [
    path("index", views.index, name="index-paws"),
]
