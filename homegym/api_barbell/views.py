from django.http import HttpResponse
from .models import Barbell
from django.core import serializers


# Create your views here.
def barbell_list(request):
  if request.method == 'GET':
    barbells = Barbell.objects.all()
    JSONSerializer = serializers.get_serializer("json")
    json_serializer = JSONSerializer()
    json_serializer.serialize(barbells)
    data = json_serializer.getvalue()
    return HttpResponse(data)