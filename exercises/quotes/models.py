from __future__ import unicode_literals

from django.db import models

class Recept(models.Model):
    recept_name = models.CharField(max_length=50)
    recept_aantalCalorien = models.CharField(max_length=50)
    recept_ingredienten = models.CharField(max_length=50)
    recept_benodigdeTijd = models.CharField(max_length=50)

    def __str__(self):
        return self.name
