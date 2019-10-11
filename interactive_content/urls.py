from django.conf.urls import url

from . import views

app_name = 'interactiveContent'


urlpatterns = [
    url(r'^courses/$', views.courses_view, name='resources'),
    url(r'^generate-content/', views.ContentCreator.as_view(), name='create_content'),
    url(r'^interactive_content/$', views.contents_view, name='interactive_content'),
    url(r'^courses/(?P<content_id>\d+)/$', views.courses_content_view, name='courses')
]
