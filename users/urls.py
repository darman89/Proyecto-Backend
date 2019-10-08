from django.conf.urls import url
from users.views import ProfesorViewSet
from rest_framework import routers
from django.urls import include, path

app_name = 'users'
router = routers.DefaultRouter()
router.register(r'profesores', ProfesorViewSet, base_name='profesores')


urlpatterns = [
    path('', include(router.urls)),
]

