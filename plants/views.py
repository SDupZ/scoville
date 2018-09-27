from rest_framework import viewsets
from .models import Plant, PlantDataPoint
from .serializers import PlantSerializer, PlantDataPointSerializer

class PlantViewSet(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PlantDataPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = PlantDataPoint.objects.all()
    serializer_class = PlantDataPointSerializer