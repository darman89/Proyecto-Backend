from django.conf.urls import url
from interactive_content.views import CursoViewSet
from rest_framework import routers
from django.urls import include, path
from . import views

app_name = 'interactiveContent'

router = routers.DefaultRouter()
router.register(r'cursos', CursoViewSet, base_name='cursos')

urlpatterns = [
    path('', include(router.urls)),
    url(r'^interactive_content/$', views.contents_view, name='interactive_content'),
    url(r'^courses/$', views.courses_view, name='courses')
]
