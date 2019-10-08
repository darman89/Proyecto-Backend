from django.conf.urls import url
from interactive_content.views import CursoViewSet
from rest_framework import routers
from django.urls import include, path


app_name = 'interactiveContent'

router = routers.DefaultRouter()
router.register(r'cursos', CursoViewSet, base_name='cursos')

urlpatterns = [
    path('', include(router.urls)),
]
