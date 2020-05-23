from django.contrib import admin

# Register your models here.
from base.admin import BaseAdmin
from .models import State, City


class CityAdmin(BaseAdmin):
    fields = ('name', 'state')



admin.site.register(City, CityAdmin)

