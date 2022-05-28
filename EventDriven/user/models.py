from django.db import models
from event.models import Zone, Show

# Create your models here.
class Ticket(models.Model):
    showid = models.ForeignKey(Show, on_delete=models.CASCADE)
    zone_name = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True)


class User(models.Model):
    date_of_birth = models.DateTimeField()
    name = models.CharField(max_length=255)
    ticketid = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ticketid) + " TicketID: " + self.name


