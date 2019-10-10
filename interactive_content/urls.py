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
    url(r'^recursos/$', views.contents_view, name='resources'),
    url(r'^cursos/$', views.courses_view, name='resources'),
    url(r'^generate-content/', views.ContentCreator.as_view(), name='create_content'),
]
