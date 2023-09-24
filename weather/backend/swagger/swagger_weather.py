from drf_yasg import openapi

# define paramters of the swagger
param_station_id = openapi.Parameter(
    "station_id",
    openapi.IN_QUERY,
    description="weather station id",
    type=openapi.TYPE_STRING,
)

param_date = openapi.Parameter(
    "date",
    openapi.IN_QUERY,
    description="weather date",
    type=openapi.TYPE_STRING,
    required=True,
    pattern="YYYY-mm-dd",
)

param_page = openapi.Parameter(
    "page",
    openapi.IN_QUERY,
    description="current page",
    type=openapi.TYPE_INTEGER,
    default=1,
)

param_limit = openapi.Parameter(
    "limit",
    openapi.IN_QUERY,
    description="the number of records in a page",
    type=openapi.TYPE_INTEGER,
    default=15,
)

# define data schema
data_schema = openapi.Schema(
    type=openapi.TYPE_ARRAY,
    items=openapi.Items(
        type=openapi.TYPE_OBJECT,
        properties={
            "station_id": openapi.Schema(type=openapi.TYPE_STRING),
            "date": openapi.Schema(type=openapi.TYPE_STRING),
        },
    ),
    description="weather data",
)

# define reponse schema
weather_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "current_page": openapi.Schema(
            type=openapi.TYPE_INTEGER,
        ),
        "total_page": openapi.Schema(
            type=openapi.TYPE_INTEGER,
        ),
        "data": data_schema,
    },
    example={
        "current_page": 1,
        "total_page": 11,
        "data": [
            {
                "id": "4d1719b5-7603-4690-857d-6e10c66d4dc3",
                "station_id": "USC00110072",
                "date": "1985-01-01",
                "temp_max": -22,
                "temp_min": -128,
                "precipitation": 94,
            }
        ],
    },
)
