from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from activities.models import Calificacion

@csrf_exempt
def list_calificacion(request):
    calificaciones = []
    return HttpResponse(serializers.serialize('json', calificaciones))