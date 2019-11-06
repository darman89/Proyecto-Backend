from rest_framework import serializers

from activities.models import PreguntaOpcionMultiple, RespuestmultipleEstudiante, Opcionmultiple, Calificacion, Marca


class OpcionMultipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcionmultiple
        fields = '__all__'

class PreguntaSeleccionMultipleSerializer(serializers.ModelSerializer):

    opciones = OpcionMultipleSerializer(many=True, read_only=True)

    class Meta:
        model = PreguntaOpcionMultiple
        fields = ['id', 'nombre', 'numeroDeIntentos', 'tieneRetroalimentacion',
                  'retroalimentacion', 'enunciado', 'esMultipleResp', 'marca', 'opciones']

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


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

