
from django.urls import path, include

from greened import views

urlpatterns = [
        path('', views.index, name='index')
]

