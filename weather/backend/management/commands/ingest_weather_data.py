from django.core.management.base import BaseCommand
from ...models import Weather
import glob
import pandas as pd
from datetime import datetime

"""ingest weather raw data into the database"""


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # read all text files in wx_data folder
        file_list = glob.glob("../wx_data/*txt")

        # create empty list for weather data
        weather_data = []
        # looping through each file (station_id)
        for f in file_list:
            # extract station_id from the current file name
            station_id = f.split("\\")[1].strip(".txt")
            print(f"reading {station_id} data...")
            # read current text file as a data frame handling inconsistent white space
            df = pd.read_csv(f, sep="\s+", header=None)

            # looping though each row of the current dataframe
            for idx, row in df.iterrows():
                # append each row to Weather object
                weather_data.append(
                    Weather(
                        station_id=station_id,
                        date=datetime.strptime(str(row[0]), "%Y%m%d").date(),
                        temp_max=int(row[1]),
                        temp_min=int(row[2]),
                        precipitation=int(row[3]),
                    )
                )
        # load into the database
        Weather.objects.bulk_create(weather_data)
