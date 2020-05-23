
from django.urls import path, include
from django.views.generic import TemplateView

from greened.views import *

urlpatterns = [
        #path('',
            #TemplateView.as_view(template_name="city.html")
            #CitiesView.as_view()
            #CityListView.as_view()
        #),
        path('greened/city/<int:city_id>/branch/<int:branch_id>/', branch_people, name="branch_people"),
        path('greened/city/<int:city_id>/', details, name="details"),
        path('greened/', index, name='index'),
        path('', index, name='index'),
]

