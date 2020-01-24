from django.db import models
from django.contrib.gis.db import models as gismodels

# Create your models here.

class Blog(models.Model):
    content = models.CharField(max_length=140, verbose_name='本文')
    posted_date = models.DateTimeField(auto_now_add=True)


class LeafletMap(gismodels.Model):
    wmoid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)

    geom = gismodels.PointField()
    #objects = gismodels.GeoManager()

    def __unicode__(self):
        return self.name
