from django.urls import path
from interactive_content.views import ContInteractivoView

app_name = 'contenido_interactivo'
# add url path to the API
urlpatterns = [
    path('cont_interactivo', ContInteractivoView.as_view(), name='cont_interactivo'),
]
