from .models import Variables
from rest_framework import serializers


class VariablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variables
        fields = "__all__"
