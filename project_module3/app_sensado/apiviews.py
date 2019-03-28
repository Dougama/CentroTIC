from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.views.defaults import bad_request
from django.shortcuts import get_object_or_404

from .models import Sensores, Tarjetas, Temperatura, Gases
from .serializers import SensoresSerializer, TarjetasSerializer, TemperaturaSerializer, GasesSerializer


class ListaSensores(APIView):
    """Usando APIView """
    authentication_classes = ()
    permission_classes = ()
    def get(self, request, pk):
        sensores = get_object_or_404(Sensores, pk=pk)
        datos = SensoresSerializer(sensores).data
        return Response(datos)
        
    def delete(self, request, pk, format=None):
        sensores = get_object_or_404(Sensores, pk=pk)
        sensores.delete()
        return Response({"respuesta": "sensor borrado"})

class ListaTarjetas(APIView):
    authentication_classes = ()
    permission_classes = ()
    def delete(self, request,pk,format=None):
        tarjetas = get_object_or_404(Tarjetas, pk=pk)
        tarjetas.delete()
        return Response({"respuesta": "tarjeta borrada"})

    def get(self, request, pk):
        tarjetas = get_object_or_404(Tarjetas, pk=pk)
        datos = TarjetasSerializer(tarjetas).data
        return Response(datos)

class ListaSensores_generics(generics.ListCreateAPIView):
    """Clase relacionada con los sensores
    usando generics """
    authentication_classes = ()
    permission_classes = ()
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
 
class ListaTarjetas_generics(generics.ListCreateAPIView):
    """Clase relacionada con las tarjetas que se comportan
    como terminal IoT usando generics"""
    authentication_classes = ()
    permission_classes = ()
    queryset = Tarjetas.objects.all()
    serializer_class = TarjetasSerializer

class ListaTemperaturas(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Temperatura.objects.all()
    serializer_class = TemperaturaSerializer

class ListaGases(generics.ListCreateAPIView):
    """
    Clase encargada de la API para las lecturas de gas
    """
    authentication_classes = ()
    permission_classes = ()
    queryset = Gases.objects.all()
    serializer_class = GasesSerializer


