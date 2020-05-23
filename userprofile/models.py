from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from base.models import Base
from cities.models import City
from companies.models import Branch

class UserProfile(Base):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.PositiveIntegerField(10)
    work_type = models.CharField(default=None)
    branch = models.ForeignKey(Branch)
    city = models.ForeignKey(City)
    
    #location = models.CharField(max_length=30, blank=True)
    #birthdate = models.DateField(null=True, blank=True)
    #role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username
