from django.shortcuts import render

# Create your views here.
def index(request):
    respuesta = {}
    return render(request, "app_praes/index.html", respuesta)