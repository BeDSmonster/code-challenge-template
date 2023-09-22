from django.db import models
import uuid


# Craete models
class Weather(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    station_id = models.CharField(max_length=15)
    date = models.DateField(null=False, blank=False)
    temp_max = models.IntegerField(default=-999)
    temp_min = models.IntegerField(default=-999)
    precipitation = models.IntegerField(default=-999)

    class Meta:
        db_table = "weather"
        unique_together = (("station_id", "date"),)


class Stats(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    station_id = models.CharField(max_length=15)
    year = models.SmallIntegerField()
    temp_max_avg = models.FloatField()
    temp_min_avg = models.FloatField()
    precipitation_accum = models.IntegerField()

    class Meta:
        db_table = "stats"
        unique_together = (("station_id", "year"),)
