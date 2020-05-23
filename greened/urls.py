
from django.urls import path, include
from django.views.generic import TemplateView

from greened.views import *

urlpatterns = [
        #path('',
            #TemplateView.as_view(template_name="city.html")
            #CitiesView.as_view()
            #CityListView.as_view()
        #),
        path('greened/city/<int:city_id>/', details, name="details"),
        path('greened/', index, name='index'),
        path('', index, name='index'),
]

