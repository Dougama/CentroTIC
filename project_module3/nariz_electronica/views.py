from django.shortcuts import render

# Create your views here.
def index(request):
    respuesta = {}
    return render(request, "nariz_electronica/index.html", respuesta)