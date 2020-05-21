from django.db import models

# Create your models here.

from base.models import BaseModel
#from base.includes import *
from city.models import City

class Company(BaseModel):
    """
    """
    name = models.CharField()
    #address = models.CharField()
    #pincode = models.PositiveIntegerField()
    #area_square_meters = models.PositiveIntegerField() # Area of company in Square-Meters


class Branch(BaseModel):
    """
    """
    name = models.CharField()
    address = models.CharField()
    pincode = models.PositiveIntegerField()
    area_square_meters = models.PositiveIntegerField() # Area of company in Square-Meters
    company = models.ForeignKey(Company)
    city = models.ForeignKey(City)

    #contact_number
    #contact_email
