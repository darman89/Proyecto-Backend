from rest_framework import serializers
from interactive_content.models import ContenidoInteractivo


class ContInteractivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContenidoInteractivo
        fields = ('id', 'contenido', 'fecha_creacion', 'tiempo_disponibilidad', 'tiene_retroalimentacion', 'curso')
    
    def create(self, validated_data):
        return ContenidoInteractivo.objects.create(**validated_data)

