from django.db import models

# Create your models here.
from base.models import Base

class State(Base):
    name = models.CharField(max_length=256)

class City(Base):
    name = models.CharField(max_length=256)
    latitude = models.DecimalField(decimal_places=7, max_digits=10)
    longitude = models.DecimalField(decimal_places=7, max_digits=10)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    area_square_meters = models.PositiveIntegerField() # Area in Square-Meters


#class CityBranch(BaseModel):
    #pass


