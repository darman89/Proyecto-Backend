from rest_framework import serializers
from activities.models import Marca, Actividad, Pregunta, Respuestmultiple


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('nombre', 'punto', 'contenido')

    def create(self, validated_data):
        return Marca.objects.create(**validated_data)
