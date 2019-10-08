from django.urls import path
from activities.views import MarcaView

app_name = 'marca'
# add url path to the API
urlpatterns = [
    path('marca', MarcaView.as_view(), name='marca'),
]
