from .models import Weather, Stats
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.core.paginator import Paginator
from rest_framework.views import APIView
from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .swagger.swagger_weather import *
from .swagger.swagger_stats import *


class WeatherView(APIView):
    @swagger_auto_schema(
        manual_parameters=[param_station_id, param_year, param_page, param_limit],
        operation_description="GET /api/weather/",
        responses={200: openapi.Response("response description", weather_response)},
    )
    def get(self, request, format=None):
        date = request.query_params.get("date")
        station_id = request.query_params.get("station_id")
        page = int(request.query_params.get("page", 1))
        limit = int(request.query_params.get("limit", 15))
        filter_param = {"date": date}

        if station_id:
            filter_param["station_id"] = station_id

        weather_data = Weather.objects.filter(**filter_param)
        paged_weather_data = Paginator(weather_data.values(), limit)
        weather_data_result = paged_weather_data.page(page)
        data = {
            "current_page": page,
            "total_page": int(paged_weather_data.count / limit) + 1,
            "data": list(weather_data_result),
        }

        return JsonResponse(data)


class StatsView(APIView):
    @swagger_auto_schema(
        manual_parameters=[param_station_id, param_year, param_page, param_limit],
        operation_description="GET /api/weather/stats",
        responses={200: openapi.Response("response description", weather_response)},
    )
    def get(self, request, format=None):
        station_id = request.query_params.get("station_id")
        year = request.query_params.get("year")
        page = int(request.query_params.get("page", 1))
        limit = int(request.query_params.get("limit", 15))
        stats_data = Stats.objects.filter(station_id=station_id, year=year)
        filter_param = {"year": year}

        if station_id:
            filter_param["station_id"] = station_id

        stats_data = Stats.objects.filter(**filter_param)
        paged_stats_data = Paginator(stats_data.values(), limit)
        weather_data_result = paged_stats_data.page(page)
        data = {
            "current_page": page,
            "total_page": int(paged_stats_data.count / limit) + 1,
            "data": list(weather_data_result),
        }

        return JsonResponse(data)
