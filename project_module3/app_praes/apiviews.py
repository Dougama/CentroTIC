from rest_framework import generics 
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from .models import Temperatura, Humedad, PresionAtmosferica, MaterialParticulado, NO2, \
      Polvo, O3, SO2, CO, CO2, MetanoPropanoCO, LuzUV, MaterialOrganico, CH4, Anemometro
from .serializers import TemperaturaSerializer, HumedadSerializer, PresionAtmosfericaSerializer, \
      MaterialParticuladoSerializer, NO2Serializer, PolvoSerializer, O3Serializer, SO2Serializer, \
      COSerializer, CO2Serializer, MetanoPropanoCOSerializer, LuzUVSerializer,\
      MaterialOrganicoSerializer, CH4Serializer, AnemometroSerializer, UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class CrearUsuarioAPI(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class TemperaturaAPI(generics.ListCreateAPIView):
    #authentication_classes = ()
    #permission_classes = ()
    queryset = Temperatura.objects.all()
    serializer_class = TemperaturaSerializer