from django.contrib import admin
from django.urls import path, include
from measurements.views import ProjectViewSet, MeasurementViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('objects', ProjectViewSet)
router.register('measurement', MeasurementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(router.urls))
]
