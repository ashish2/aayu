from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
from cities.models import City
from companies.models import Branch
from algo import algo

class CitiesView(TemplateView):
    template_name = "city.html"

class CityListView(TemplateView):
    model = City

def index(request):
    cities = City.objects.all()

    context = {'cities': cities}

    return render(request, 'index.html', context)


def details(request, city_id):
    city = City.objects.get(id=city_id)
    branches = city.branch_set.all()

    context = {'city': city, 'branches': branches}

    return render(request, 'details.html', context)

def branch_people(request, city_id, branch_id):
    city = City.objects.get(id=city_id)
    branch = Branch.objects.get(id=branch_id)

    min_dist = algo.minimum_distance_to_be_maintained()
    handle = round( algo.how_many_can_be_handled(branch.area) )

    allowed_handle = round( handle - (handle * 20/100) )

    context = {
        'city': city,
        'branch': branch,
        'min_dist': min_dist,
        'handle': handle,
        'allowed_handle': allowed_handle,
        'not_allowed_handle': round( handle - allowed_handle ),
    }

    return render(request, 'branch_people.html', context)
