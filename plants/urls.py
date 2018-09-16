from django.urls import path
from .views import ListPlantsView

urlpatterns = [
  path('plants/', ListPlantsView.as_view(), name="plants-all")
]
