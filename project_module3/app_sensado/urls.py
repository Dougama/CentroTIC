from django.urls import path 
from . import views
from . import apiviews

app_name = "app_sensado"
urlpatterns = [
    path("accion_raspberry", views.accion_raspberry, name="accion-raspberry"),
    path("presentacion-datos", views.presentacion_datos, name="datos-fecha"),
    path("presentacion-datos-json", views.presentacion_datos_json, name="datos-json"),
    path('sensores-generic/', apiviews.ListaSensores_generics.as_view(), name="lista-sensores-generics"),
    path("sensores-generic/<int:pk>/", apiviews.ListaSensores.as_view()), 
    path('tarjetas-generic/', apiviews.ListaTarjetas_generics.as_view(), name="lista-tarjetas-generics"),
    path('tarjetas-generic/<int:pk>/', apiviews.ListaTarjetas.as_view()),
    path('lista-temperaturas/', apiviews.ListaTemperaturas.as_view()),
    path('lista-gases/', apiviews.ListaGases.as_view()),
    path('historico-datos/', views.historico_datos, name="historico-datos"),
    path('historico-datos-json/', views.historico_datos_json, name="historico-datos-json"),
    path('index/', views.index, name="index"),
]
