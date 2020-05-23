from django.db import models
from django.db.models import signals 
# Create your models here.
from django.contrib.auth.models import User
from base.models import Base
from cities.models import City
from companies.models import Branch

from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(Base):

    class WorkType(models.TextChoices):
        LA = ('LA', 'LABOUR'),
        IT = ('IT', 'INFO TECH')

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.PositiveIntegerField(10, default=None)
    work_type = models.CharField( choices=WorkType.choices, default=WorkType.LA)
    branch = models.ForeignKey(Branch, default=1)
    city = models.ForeignKey(City, default=1)
    
    #location = models.CharField(max_length=30, blank=True)
    #birthdate = models.DateField(null=True, blank=True)
    #role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

# SAVE SIGNAL
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




