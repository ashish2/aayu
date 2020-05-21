from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from base.models import BaseModel
from city.models import City

class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #location = models.CharField(max_length=30, blank=True)
    city = models.ForeignKey(City)
    
    #birthdate = models.DateField(null=True, blank=True)
    #role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username
