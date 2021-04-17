from django.contrib.gis.db import models

# Create your models here.
class BerlinLocations(models.Model):
    name = models.CharField(max_length=50, null=False)
    geom = models.PointField(srid = 4326)