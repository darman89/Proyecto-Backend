from django.urls import path
from activities import views
app_name = 'activities'

urlpatterns = [
    path('calificacion', views.list_calificacion, name='calificacion'),
]