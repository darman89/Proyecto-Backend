from django.shortcuts import render
from rest_framework import viewsets
from users.models import Profesor
from users.serializers import ProfesorSerializer
# Create your views here.


class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
