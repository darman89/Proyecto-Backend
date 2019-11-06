from activities.views import MarcaView, ActividadView, RespEstudianteMultipleView, reports
from django.urls import path

app_name = 'marca'
# add url path to the API
urlpatterns = [
    path('marca', MarcaView.as_view(), name='marca'),
    path('actividad', ActividadView.as_view(), name='actividad'),
    path('resp_estudiante_op_multiple', RespEstudianteMultipleView.as_view(), name='respuesta_estd_op_multiple'),
    path('reports/', reports, name='reports'),
]