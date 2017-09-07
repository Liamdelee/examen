from django.shortcuts import render
from .models import Recept
from mongoengine import *

connect('test', host='mongodb://localhost/test')

def list_all_recepten(request):
    recepten = Recept.objects.all()
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
        try:
            recept = Recept(recept_name = "test", recept_aantalCalorien = "test", recept_ingredienten = "test", recept_benodigdeTijd = "test").save()
            return render(request, 'quotes/ok.html', None)
        except:
            return render(request, 'quotes/index.html', None)
    else:
        return render(request, 'quotes/add.html', None)
