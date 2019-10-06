from django.shortcuts import render
from rest_framework import viewsets
from interactive_content.models import Curso
from interactive_content.serializers import CursoSerializer

# Create your views here.


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
