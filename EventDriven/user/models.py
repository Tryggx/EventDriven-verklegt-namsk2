from django.db import models
from django.contrib.auth.models import AbstractUser
from event.models import Zone, Show

# Create your models here.


class User(AbstractUser):
    """Add more parameters to deafult django user"""
    date_of_birth = models.DateField(null=True)
    profile_picture = models.ImageField(upload_to='static/img/profile-pics', blank=True, null=True)

    def __str__(self):
        return self.username

class Ticket(models.Model):
    showid = models.ForeignKey(Show, on_delete=models.CASCADE)
    zone_name = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
