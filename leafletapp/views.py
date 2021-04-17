from rest_framework_gis.pagination import GeoJsonPagination
from rest_framework import generics
from .models import BerlinLocations
from .serializer import BerlinLocationsSerializer

# Create your views here.
class BerlinLocationsList(generics.ListCreateAPIView):
    queryset = BerlinLocations.objects.all()
    serializer_class = BerlinLocationsSerializer
    pagination_class = GeoJsonPagination