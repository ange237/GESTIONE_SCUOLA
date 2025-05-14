from django.shortcuts import render
from .models import Risultato_esame_corso
from django.db.models import Q
from studente.views import *
from corso.views import *
from corso.models import *

"""Risultato_esame_corso.objects.create(id_studente=1, id_corso=2, voto =29)
Risultato_esame_corso.objects.create(id_studente=2, id_corso=1, voto =28)
Risultato_esame_corso.objects.create(id_studente=2, id_corso=3, voto =20)
Risultato_esame_corso.objects.create(id_studente=3, id_corso=1, voto =26)"""

#funzione per ottener tutti i risultati
def lista_risultati(request):
    risultati = Risultato_esame_corso.objects.all()
    return render(request,"studente/lista_risultati.html",{"risultati":risultati})

#funzione per creare un nuovo risultato
def add_risultato_esame(id_stud,id_esa,voto):
    risultato = Risultato_esame_corso.objects.create(id_studente=id_stud, id_esame=id_esa, voto =voto)
    return "risultato registrato con successo."

#funzione per cancellare un risultato
def del_risultato_esame(id_stud,id_esa):
    risultato = Risultato_esame_corso.objects.filter(Q(id_studente = id_stud) & Q(id_esame = id_esa))
    risultato.delete()

#funzione per modificare il voto di un esame
def modifica_risultato_esame(id_stud,id_esa,voto):
    risultato = Risultato_esame_corso.objects.filter(Q(id_studente = id_stud) & Q(id_esame = id_esa))
    risultato.voto = voto
    risultato.save()


#funzione per ottenere dato uno studente tutti i suoi risultati
def lista_risultati_studente(id_studente):
  lista = Risultato_esame_corso.objects.filter(id_studente = id_studente)
  map = {} #mappa con nome corso- voto
  for i in lista:
     map[get_corso(i.id_corso).get_name()] =i.voto
  return map #ritorna una lista di risultato_esame_corso in somma una lista di oggetti della classe di origine.

#funzione per ottenere dato un corso tutti i suoi risultati
def lista_risultati_corso(id_corso):
     lista = Risultato_esame_corso.objects.filter(id_corso = id_corso)
     return lista


