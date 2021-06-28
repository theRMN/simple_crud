import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse, JsonResponse
from .models import Project, Measurement


# class ProjectViewSet(ModelViewSet):
#     """ViewSet для проекта."""
#     # TODO: добавьте конфигурацию для объекта
#
#
# class MeasurementViewSet(ModelViewSet):
#     """ViewSet для измерения."""
#     # TODO: добавьте конфигурацию для измерения

@csrf_exempt
def object_view(request):
    if request.method not in ['GET', 'POST']:
        return HttpResponse(status=405)

    if request.method == 'GET':
        objects = Project.objects.all()
        data = [{'name': obj.name, 'latitude': obj.latitude, 'longitude': obj.longitude} for obj in objects]

        return JsonResponse(data, status=200, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        obj = Project.objects.create(**data)
        context = {'name': obj.name, 'latitude': obj.latitude, 'longitude': obj.longitude}

        return JsonResponse(context, status=201)
