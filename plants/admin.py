from django.contrib import admin
from plants.models import Plant, PlantDataPoint


class PlantDataPointInline(admin.StackedInline):
    model = PlantDataPoint
    extra = 1


class PlantAdmin(admin.ModelAdmin):
    inlines = [PlantDataPointInline]

admin.site.register(Plant, PlantAdmin)