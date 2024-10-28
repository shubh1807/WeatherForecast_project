# WeatherForecast/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forecast.urls')),  # Include URLs from the forecast app
]
