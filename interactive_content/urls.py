from django.conf.urls import url
from django.urls import path
from interactive_content import views

app_name = 'interactiveContent'


urlpatterns = [
    url(r'^recursos/$', views.contents_view, name='resources'),
    url(r'^courses/$', views.courses_view, name='resources'),
    url(r'^generate-content/', views.ContentCreator.as_view(), name='create_content'),
    url(r'^interactive_content/$', views.contents_view, name='interactive_content'),
    path('cont_interactivo', views.ContInteractivoView.as_view(), name='cont_interactivo'),
    url(r'^courses/(?P<content_id>\d+)/$', views.courses_content_view, name='courses')
]