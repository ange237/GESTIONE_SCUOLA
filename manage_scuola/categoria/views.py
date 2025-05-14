from django.shortcuts import render
from .models import Categoria

"""Categoria.objects.create(name="scienze matematiche")
Categoria.objects.create(name="scienze umane")
Categoria.objects.create(name="IT and Tecnology")
Categoria.objects.create(name="lingue")"""

#funzione per creare una nuova categoria
def add_category(name):
    Categoria.objects.create(name=name)
    return "categoria creata con successo."

#funzione per cancellare una categoria 
def del_category(id_category):
  categoria =  Categoria.objects.get(id=id_category)
  categoria.delete()
  return "categoria cancellata con successo."


#funzione per ottenere una categoria dato il suo id
def get_category(id_category):
   categoria =  Categoria.objects.get(id=id_category)
   return categoria

#funzione per stampare tutte le categorie di corso
def lista_category(request):
  categorie = Categoria.objects.all()
  return render(request,'studente/lista_categorie.html',{'categorie':categorie})