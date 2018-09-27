from django.urls import path, include
from rest_framework import routers
from .views import PlantViewSet, PlantDataPointViewSet

router = routers.DefaultRouter()
router.register(r'plants', PlantViewSet)
router.register(r'plant-data', PlantDataPointViewSet)

urlpatterns = router.urls
