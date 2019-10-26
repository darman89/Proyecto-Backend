from activities.views import *
from django.urls import path
from activities.views import CalificarAPI
app_name = 'activities'

urlpatterns = [    
    path('preguntaOpcionMultiple/<int:pk>/', DetailPreguntaSeleccionMultiple.as_view())
    path('calificacion', CalificarAPI.as_view(), name='calificacion'),
]