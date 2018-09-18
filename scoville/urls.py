from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/', include('plants.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
