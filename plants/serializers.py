from rest_framework import serializers
from .models import Plant, PlantDataPoint

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'


class PlantDataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantDataPoint
        fields = '__all__'