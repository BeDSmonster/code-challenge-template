from django.core.management.base import BaseCommand
from ...models import Weather, Stats
import pandas as pd


"""create summary statistics from weather data"""


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # retrieving unique station_id from Weather object
        station_id_list = list(set(Weather.objects.values_list("station_id")))
        # create empty list for calculated statistics data
        stat_data = []
        # looping through unique station _id
        for s in station_id_list:
            station_id = s[0]  # current station_id
            # query the object of the current station_id
            q = Weather.objects.filter(station_id=station_id)
            df = pd.DataFrame(q.values())
            # extract year from datetime
            df["year"] = df["date"].apply(lambda x: x.year)

            # calculate statistics
            ## for every station_id and year, calculate mean of max temperature and min temperature
            ## and accumulated precipitation
            station_stat_df = (
                df.groupby(["year"])
                .agg({"temp_max": "mean", "temp_min": "mean", "precipitation": "sum"})
                .reset_index()
            )

        # looping though each row of statistics dataframe
        for idx, row in station_stat_df.iterrows():
            stat_data.append(
                Stats(
                    station_id=station_id,
                    year=int(row["year"]),
                    temp_max_avg=int(row["temp_max"]),
                    temp_min_avg=int(row["temp_min"]),
                    precipitation_accum=int(row["precipitation"]),
                )
            )
        # load into the database
        Stats.objects.bulk_create(stat_data)
