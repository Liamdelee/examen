from django.shortcuts import render
from .models import Recept
from mongoengine import *

connect('test', host='mongodb://localhost/test')

def list_all_recepten(request):
    recepten = Recept.objects
    context = {'recepten': recepten}
    return render(request, 'quotes/index.html', context)

#def search(request):
#    if request.method == 'POST':
#        author_name = request.POST.get('name').title() # Capitalize name
#        try:
#            author = Author.objects.get(name=author_name)
#            quotes = Quote.objects.filter(author_id=author.id)
#            context = {'quotes': quotes}
#            return render(request, 'quotes/index.html', context)
#        except:
#            return render(request, 'quotes/index.html', None)
#    else:
#        return render(request, 'quotes/search.html', None)

def add(request):
    if request.method == 'POST':
        recept = request.POST.get('recept').title()
        receptsplit = recept.split(",")
        recept_name = receptsplit[0]
        recept_aantalCalorien = int(receptsplit[1])
        recept_ingredienten = receptsplit[2]
        recept_benodigdeTijd = int(receptsplit[3])
        try:
            #Recept.Objects(recept_name____exact=recept_name) geen idee hoe vergelijken
            for recept in Recept.objects:
                if recept.recept_name == recept_name:
                    return render(request, 'quotes/add.html', None)
                else:
                    recept = Recept(recept_name = recept_name, recept_aantalCalorien = recept_aantalCalorien, recept_ingredienten = recept_ingredienten, recept_benodigdeTijd = recept_benodigdeTijd).save()
                    return render(request, 'quotes/ok.html', None)
        except:
            return render(request, 'quotes/index.html', None)
    else:
        return render(request, 'quotes/add.html', None)
