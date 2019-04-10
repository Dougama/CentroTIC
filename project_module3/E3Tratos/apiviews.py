from rest_framework import generics 
from rest_framework.response import Response

from .models import Variables
from .serializers import VariablesSerializer

class VariablesAPI(generics.CreateAPIView):
    queryset = Variables.objects.all()
    serializer_class = VariablesSerializer