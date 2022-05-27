from django.db import models
from event.models import Zone, Show

# Create your models here.

class User(models.Model):
    date_of_birth = models.DateTimeField()
    name = models.CharField(max_length=255)
    ticketid = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ticketid) + " TicketID: " + self.name

class Ticket(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    showid = models.ForeignKey(Show, on_delete=models.CASCADE)
    zone_name = models.ForeignKey(Zone.name)

