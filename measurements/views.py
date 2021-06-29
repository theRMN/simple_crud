from .models import Project, Measurement
from .serializers import ProjectSerializer, MeasurementSerializer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.response import Response
from rest_framework.views import APIView

# class ProjectViewSet(ModelViewSet):
#     """ViewSet для проекта."""
#     # TODO: добавьте конфигурацию для объекта
#
#
# class MeasurementViewSet(ModelViewSet):
#     """ViewSet для измерения."""
#     # TODO: добавьте конфигурацию для измерения


class ProjectApiView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Project.objects.all()
        serializer = ProjectSerializer(objects, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = Project.objects.create(**serializer.validated_data)
        context = ProjectSerializer(obj)
        return Response(context.data, status=HTTP_201_CREATED)
