from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Variables

# Create your views here.
def index(request):
    respuesta = {}
    return render(request, "E3Tratos/index.html", respuesta)

@csrf_exempt
def datos_json(request):
    var = Variables.objects.all()
    datos = var.values("fecha", "variables")
    datos = list(map(lambda datos: [datos["fecha"], datos["variables"]], datos))

    respuesta = {"datos": datos}
    return JsonResponse(respuesta)