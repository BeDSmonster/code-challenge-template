from django.core.management.base import BaseCommand
from ...models import Weather
import glob
import pandas as pd
from datetime import datetime
import logging
import time

"""ingest weather raw data into the database"""

# configure logging
log_format = "[%(levelname)s | %(asctime)s] - %(message)s"
logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("ingest_data_execution.log", "a", "utf-8"),
        logging.StreamHandler(),
    ],
)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # read all text files in wx_data folder
        file_list = glob.glob("../wx_data/*txt")

        # create empty list for weather data
        weather_data = []
        start_time = time.time()
        # looping through each file (station_id)
        for f in file_list:
            # extract station_id from the current file name
            station_id = f.split("\\")[1].strip(".txt")
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
        Weather.objects.bulk_create(weather_data, ignore_conflicts=True)
        end_time = time.time()
        # measure data ingesting execution time
        exe_time = end_time - start_time
        # log info
        logging.info(f"{len(weather_data)} records ingestion ran in {exe_time}s")
