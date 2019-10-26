from rest_framework.generics import ListCreateAPIView

from activities.serializers import CalificacionSerializer
from activities.models import Calificacion


class CalificarAPI(ListCreateAPIView):
    # serializer usado para la transformacion de datos
    serializer_class = CalificacionSerializer
    # filtro de estudiante
    filterset_fields = ("estudiante", "actividad")

    def get_queryset(self):
        # queryset para retornar las calificaciones de un estudiante
        return Calificacion.objects.all()
