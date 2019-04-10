from django.urls import path 
from .apiviews import VariablesAPI
from .views import index, datos_json

app_name = "E3Tratos"

urlpatterns = [
        path("variables-api", VariablesAPI.as_view(),name="e3tratos-api"),
        path("index", index, name="index-E3Tratos"),
        path("datos-json", datos_json, name="datos-json-E3Tratos"),
]
