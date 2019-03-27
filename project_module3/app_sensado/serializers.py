from rest_framework import serializers
from .models import Sensores, Tarjetas, Humedad, Temperatura, Gases

class SensoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensores
        fields = '__all__'

class TarjetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjetas
        fields = '__all__'

class HumedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Humedad
        fields = '__all__'

class TemperaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperatura
        fields = '__all__'

class GasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gases
        fields = '__all__'