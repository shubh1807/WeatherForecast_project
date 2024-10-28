# forecast/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Landing page with input form
    path('forecast/', views.forecast, name='forecast'),  # Forecast result page
]
