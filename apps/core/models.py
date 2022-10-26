from django.db import models

# Create your models here.

class Gisement(models.Model):
    name = models.CharField(max_length=50)


class Site(models.Model):
    adr = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=60)
    gisement = models.ForeignKey(Gisement, on_delete=models.CASCADE, related_name="site")
