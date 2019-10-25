from django.urls import path
from activities.views import CalificarAPI
app_name = 'activities'

urlpatterns = [
    path('calificacion', CalificarAPI.as_view(), name='calificacion'),
]