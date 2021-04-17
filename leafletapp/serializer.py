from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import BerlinLocations

class BerlinLocationsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BerlinLocations
        id_field = 'id'
        geo_field = 'geom'
        fields = '__all__'