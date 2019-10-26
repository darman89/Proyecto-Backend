from rest_framework import serializers

from activities.models import PreguntaOpcionMultiple, RespuestmultipleEstudiante, Opcionmultiple, Calificacion


class PreguntaSeleccionMultipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreguntaOpcionMultiple
        fields = '__all__'

    def create(self, validated_data):
        return PreguntaOpcionMultiple.objects.create(**validated_data)


class RespuestaSeleccionMultipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestmultipleEstudiante
        fields = '__all__'
      

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = ('id', 'estudiante', 'actividad', 'calificacion')


