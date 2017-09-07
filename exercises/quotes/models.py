from __future__ import unicode_literals

from mongoengine import *

class Recept(Document):
    recept_name = StringField(max_length=50)
    recept_aantalCalorien = StringField(max_length=50)
    recept_ingredienten = StringField(max_length=50)
    recept_benodigdeTijd = StringField(max_length=50)

    def __str__(self):
        return self.name
