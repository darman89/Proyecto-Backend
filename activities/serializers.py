from rest_framework import serializers
from activities.models import PreguntaOpcionMultiple
from activities.models import Calificacion

class PreguntaSeleccionMultipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreguntaOpcionMultiple
        fields = '__all__'

    def create(self, validated_data):
        return PreguntaOpcionMultiple.objects.create(**validated_data)
      

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = ('id', 'estudiante', 'actividad', 'calificacion')

