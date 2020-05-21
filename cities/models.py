from django.db import models

# Create your models here.
from base import BaseModel

class City(BaseModel):
    name = models.CharField()
    latitude = models.DoubleField()
    longitude = models.DoubleField()
    state = models.CharField()
    area_square_meters = models.PositiveIntegerField() # Area in Square-Meters


