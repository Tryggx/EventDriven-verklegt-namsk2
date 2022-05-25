from django.db import models

# Create your models here.
class Venues(models.Model):
    name = models.CharField(255)
