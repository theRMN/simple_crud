from .models import Project, Measurement
from .serializers import ProjectSerializer, MeasurementSerializer
from rest_framework.generics import ListCreateAPIView

# class ProjectViewSet(ModelViewSet):
#     """ViewSet для проекта."""
#     # TODO: добавьте конфигурацию для объекта
#
#
# class MeasurementViewSet(ModelViewSet):
#     """ViewSet для измерения."""
#     # TODO: добавьте конфигурацию для измерения


class ProjectApiView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
