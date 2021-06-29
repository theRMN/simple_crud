from django.http import JsonResponse
from .models import Project, Measurement
from rest_framework.decorators import api_view
from .serializers import ProjectSerializer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

# class ProjectViewSet(ModelViewSet):
#     """ViewSet для проекта."""
#     # TODO: добавьте конфигурацию для объекта
#
#
# class MeasurementViewSet(ModelViewSet):
#     """ViewSet для измерения."""
#     # TODO: добавьте конфигурацию для измерения


METHODS = ['GET', 'POST']


@api_view(http_method_names=METHODS)
def object_view(request):
    if request.method == 'GET':
        objects = Project.objects.all()
        serializer = ProjectSerializer(objects, many=True)

        return JsonResponse(serializer.data, status=HTTP_200_OK, safe=False)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = Project.objects.create(**serializer.validated_data)
        context = ProjectSerializer(obj)

        return JsonResponse(context.data, status=HTTP_201_CREATED)
