from django.urls import path
from activities.views import MarcaView, ActividadView, RespEstudianteMultipleView, PreguntaView

app_name = 'marca'
# add url path to the API
urlpatterns = [
    path('marca', MarcaView.as_view(), name='marca'),
    path('actividad', ActividadView.as_view(), name='actividad'),
	path('pregunta', PreguntaView.as_view(), name='pregunta'),
    path('resp_estudiante_op_multiple', RespEstudianteMultipleView.as_view(), name='respuesta_estd_op_multiple'),
]
