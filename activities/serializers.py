from rest_framework import serializers
from activities.models import PreguntaOpcionMultiple, RespuestmultipleEstudiante, Opcionmultiple
# 
# 
# class MarcaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Marca
#         fields = ('id', 'nombre', 'punto', 'contenido')
# 
#     def create(self, validated_data):
#         return Marca.objects.create(**validated_data)
# 
# 
# class ActividadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Actividad
#         fields = ('id', 'nombre', 'numeroDeIntentos', 'tieneRetroalimentacion', 'marca')
# 
#     def create(self, validated_data):
#         return Actividad.objects.create(**validated_data)
# 
# 
# class RespuestaMultipleEstudianteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RespuestmultipleEstudiante
#         fields = ('id', 'seleccionada', 'estudiante', 'respuestmultiple')
# 
#     def create(self, validated_data):
#         return RespuestmultipleEstudiante.objects.create(**validated_data)
# 
# 
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

   
#
# 
# class RespuestaMultipleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Respuestmultiple
#         fields = ('id', 'respuesta', 'esCorrecta', 'preguntaSeleccionMultiple')          
# 
#     def create(self, validated_data):
#         return Respuestmultiple.objects.create(**validated_data)
#            