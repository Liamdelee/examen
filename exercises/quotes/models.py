from __future__ import unicode_literals

from mongoengine import *

class Recept(Document):
    recept_name = StringField(max_length=50)
    recept_aantalCalorien = IntField()
    recept_ingredienten = StringField(max_length=50)
    recept_benodigdeTijd = IntField()

    def __str__(self):
        return self.name
