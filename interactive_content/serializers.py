from rest_framework import serializers

from interactive_content.models import Contenido, Curso


class ContenidoSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField()
    url = serializers.URLField()

    class Meta:
        model = Contenido
        fields = ('id', 'nombre', 'url')


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
