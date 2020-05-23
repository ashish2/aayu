from django.db import models

# Create your models here.

from base.models import Base
#from base.includes import *
from cities.models import City

class Company(Base):
    """
    """
    name = models.CharField(max_length=256)
    #address = models.CharField()
    #pincode = models.PositiveIntegerField()
    #area_square_meters = models.PositiveIntegerField() # Area of company in Square-Meters


class Branch(Base):
    """
    """
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    pincode = models.PositiveIntegerField()
    area = models.DecimalField(decimal_places=5, max_digits=15, default=None) # Area of company in Square-Meters
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    #contact_number
    #contact_email
    def __str__(self):
        return self.name + " , City: " + self.city.name
