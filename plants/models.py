
from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=255, null=False)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
      verbose_name = "Plant"
      ordering = ('name',)


# Time series data
class PlantDataPoint(models.Model):
  plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

  sensor_id = models.CharField(max_length=255, null=False)
  sensor_name = models.CharField(max_length=255, null=False)

  soil_humidity = models.IntegerField(null=False)

  created_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return "{} {}".format(self.sensor_name, self.created_date)

  class Meta:
      verbose_name = "Plant data point"
