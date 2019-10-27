from activities.views import *
from django.urls import path
from activities.views import CalificarAPI, MarcaApi
app_name = 'activities'


app_name = 'marca'
# add url path to the API
urlpatterns = [
    path('respuestaOpcionMultiple/', RespuestaSeleccionMultipleView.as_view()),
    path('preguntaOpcionMultiple/<int:pk>/', DetailPreguntaSeleccionMultiple.as_view()),
    path('calificacion', CalificarAPI.as_view(), name='calificacion'),
    path('marca', MarcaApi.as_view(), name='marca'),
]