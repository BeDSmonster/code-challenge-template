from django.urls import path
from .views import WeatherView, StatsView


urlpatterns = [
    path("weather/", WeatherView.as_view(), name="weather"),
    path("weather/stats/", StatsView.as_view(), name="stats"),
]
