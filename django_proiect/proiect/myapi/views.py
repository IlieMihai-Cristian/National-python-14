from django.shortcuts import render
from rest_framework import viewsets

from aplicatie1.models import Location
from myapi.serializers import LocationSerializers


# Create your views here.

class LocationViewSet(viewsets.ModelViewSet):
    # list -> ofera toate resursele de un anumit tip
    # create -> creaza resurse de un anumit tip
    # retrive -> ofera o anumita resursa pe baza unui pk
    # update -> modifica o anumita resursa pe baza unui pk
    # delete -> sterge o anumita resursa pe baza unui pk
    queryset = Location.objects.all().order_by('city')
    serializer_class = LocationSerializers
