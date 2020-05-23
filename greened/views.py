from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from cities.models import City

def index(request):
    cities = City.objects.all()

    return render(cities)



