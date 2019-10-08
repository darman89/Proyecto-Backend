from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^recursos/$', views.contents_view, name='resources'),
    url(r'^cursos/$', views.courses_view, name='resources')
]
