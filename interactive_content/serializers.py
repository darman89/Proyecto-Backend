from rest_framework import serializers

from interactive_content.models import Contenido


class ContenidoSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField()
    url = serializers.URLField()

    class Meta:
        model = Contenido
        fields = ('id', 'nombre', 'url')


class CursoSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField()

    class Meta:
        model = Contenido
        fields = ('id', 'nombre')
