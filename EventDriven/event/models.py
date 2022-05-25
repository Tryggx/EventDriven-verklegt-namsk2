from django.db import models


class Event(models.Model):
    name = models.CharField(255)
    description = models.CharField(4096)
    poster_image = models.CharField(8192)
    header_image = models.CharField(8192)
    #eventttypeid = models.ForeignKey(EventType)

class Show(models.Model):
    #venueid = models.ForeignKey(Venue, on_delete=models.CASCADE)
    eventid = models.ForeignKey(Event, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

class Zone(models.Model):
    name = models.CharField(255)
    showid = models.ForeignKey(Show, on_delete=models.CASCADE)
    price = models.CharField(100)
