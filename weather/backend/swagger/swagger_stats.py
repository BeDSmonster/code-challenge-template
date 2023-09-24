from drf_yasg import openapi

# define paramters of the swagger
param_station_id = openapi.Parameter(
    "station_id",
    openapi.IN_QUERY,
    description="weather station id",
    type=openapi.TYPE_STRING,
)

param_year = openapi.Parameter(
    "year",
    openapi.IN_QUERY,
    description="weather year",
    type=openapi.TYPE_STRING,
    required=True,
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
            "year": openapi.Schema(type=openapi.TYPE_STRING),
        },
    ),
    description="weather stats data",
)

# define reponse schema
stats_response = openapi.Schema(
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
                "id": "5fa014df-194b-486c-803b-695710d356b0",
                "station_id": "USC00113879",
                "year": 1985,
                "temp_max_avg": 193,
                "temp_min_avg": 74,
                "precipitation_accum": 14473,
            }
        ],
    },
)
