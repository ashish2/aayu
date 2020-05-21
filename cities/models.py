from django.db import models

# Create your models here.
from base import BaseModel
from company import Branch

class State(BaseModel):
    name = models.CharField()

class City(BaseModel):
    name = models.CharField()
    latitude = models.DoubleField()
    longitude = models.DoubleField()
    state = models.ForeignKey(State)
    area_square_meters = models.PositiveIntegerField() # Area in Square-Meters


#class CityBranch(BaseModel):
    #pass


