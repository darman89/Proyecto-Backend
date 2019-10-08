from django.urls import path
from activities.views import MarcaView, ActividadView

app_name = 'marca'
# add url path to the API
urlpatterns = [
    path('marca', MarcaView.as_view(), name='marca'),
    path('actividad', ActividadView.as_view(), name='actividad'),
]
