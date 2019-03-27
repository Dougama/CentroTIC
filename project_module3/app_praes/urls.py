from django.urls import path 
from rest_framework.authtoken import views
from .apiviews import TemperaturaAPI, CrearUsuarioAPI, LoginView

app_name = "app_praes"
urlpatterns = [
    path('login/', views.obtain_auth_token, name="login"),
    path('usuario/', CrearUsuarioAPI.as_view(), name="crear-usuario"),
    path('temperatura/', TemperaturaAPI.as_view(), name="praes-temperatura"),
]