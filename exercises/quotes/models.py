from __future__ import unicode_literals

from mongoengine import *

class Recept(Document):
    recept_name = models.CharField(max_length=50)
    recept_aantalCalorien = models.CharField(max_length=50)
    recept_ingredienten = models.CharField(max_length=50)
    recept_benodigdeTijd = models.CharField(max_length=50)

    def __str__(self):
        return self.name
