from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255)

class Venue(models.Model):
    name = models.CharField(max_length=255)
    seating = models.IntegerField()
    accessible_seating = models.IntegerField()
    locationid = models.ForeignKey(Location, on_delete=models.CASCADE)





