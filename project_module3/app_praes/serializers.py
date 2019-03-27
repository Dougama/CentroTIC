
from .models import Temperatura, Humedad, PresionAtmosferica, \
                    MaterialParticulado, NO2, Polvo, O3, SO2, CO, CO2, \
                    MetanoPropanoCO, LuzUV, MaterialOrganico, CH4, Anemometro
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class TemperaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperatura
        fields = "__all__"

class HumedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Humedad
        fields = "__all__"

class PresionAtmosfericaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresionAtmosferica
        fields = "__all__"

class MaterialParticuladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialParticulado
        fields = "__all__"

class NO2Serializer(serializers.ModelSerializer):
    class Meta:
        model = NO2
        fields = "__all__"

class PolvoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polvo
        fields = "__all__"

class O3Serializer(serializers.ModelSerializer):
    class Meta:
        model = O3
        fields = "__all__"

class SO2Serializer(serializers.ModelSerializer):
    class Meta:
        model = SO2
        fields = "__all__"

class COSerializer(serializers.ModelSerializer):
    class Meta:
        model = CO
        fields = "__all__"

class CO2Serializer(serializers.ModelSerializer):
    class Meta:
        model = CO2
        fields = "__all__"

class MetanoPropanoCOSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetanoPropanoCO
        fields = "__all__" 

class LuzUVSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuzUV
        fields = "__all__"

class MaterialOrganicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialOrganico
        fields = "__all__"

class CH4Serializer(serializers.ModelSerializer):
    class Meta:
        model = CH4
        fields = "__all__"

class AnemometroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anemometro
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user