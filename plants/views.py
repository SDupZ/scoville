from rest_framework import generics
from .models import Plant, PlantDataPoint
from .serializers import PlantSerializer

class ListPlantsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer