from rest_framework import serializers

from interactive_content.models import Contenido, Curso, ContenidoInteractivo


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


class ContenidoInteractivoSerializer(serializers.ModelSerializer):
    contenido = ContenidoSerializer(read_only=True)

    class Meta:
        model = ContenidoInteractivo
        fields = '__all__'
