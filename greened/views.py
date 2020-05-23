from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
from cities.models import City

class CitiesView(TemplateView):
    template_name = "city.html"

class CityListView(TemplateView):
    model = City

def index(request):
    cities = City.objects.all()

    print(cities)
    context = {'data': cities}

    return render(request, 'index.html', context)


def details(request, city_id):
    data = City.objects.get(id=city_id)

    print(cities)
    context = {'data': data}

    return render(request, 'details.html', context)

