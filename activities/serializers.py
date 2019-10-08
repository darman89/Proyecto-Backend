from rest_framework import serializers
from activities.models import Marca, Actividad, Pregunta, Respuestmultiple


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id', 'nombre', 'punto', 'contenido')

    def create(self, validated_data):
        return Marca.objects.create(**validated_data)

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ('id', 'nombre', 'numeroDeIntentos', 'tieneRetroalimentacion', 'marca')

    def create(self, validated_data):
        return Actividad.objects.create(**validated_data)
