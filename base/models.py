from django.db import models


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(default=True) # status: values 0-Deactivated, 1-Active, 2-Pending, null-probably untouched yet
    class Meta:
        abstract = True
