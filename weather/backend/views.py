from .models import Weather, Stats
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.core.paginator import Paginator
from rest_framework.views import APIView
from django.http import JsonResponse


class WeatherView(APIView):
    def get(self, request, format=None):
        station_id = request.query_params.get("station_id")
        date = request.query_params.get("date")
        page = request.query_params.get("page", 1)
        limit = request.query_params.get("limit", 15)
        weather_data = Weather.objects.filter(station_id=station_id, date=date)
        paged_weather_data = Paginator(weather_data.values(), limit)
        weather_data_result = paged_weather_data.page(page)
        data = {
            "previous_page": weather_data_result.has_previous()
            and weather_data_result.previous_page_number()
            or None,
            "next_page": weather_data_result.has_next()
            and weather_data_result.next_page_number()
            or None,
            "data": list(weather_data_result),
        }

        return JsonResponse(data)


class StatsView(APIView):
    def get(self, request, format=None):
        station_id = request.query_params.get("station_id")
        year = request.query_params.get("year")
        page = request.query_params.get("page", 1)
        limit = request.query_params.get("limit", 15)
        weather_data = Stats.objects.filter(station_id=station_id, year=year)
        paged_weather_data = Paginator(weather_data.values(), limit)
        weather_data_result = paged_weather_data.page(page)
        data = {
            "previous_page": weather_data_result.has_previous()
            and weather_data_result.previous_page_number()
            or None,
            "next_page": weather_data_result.has_next()
            and weather_data_result.next_page_number()
            or None,
            "data": list(weather_data_result),
        }

        return JsonResponse(data)
