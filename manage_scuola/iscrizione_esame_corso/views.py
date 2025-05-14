from django.shortcuts import render
from .models import Iscrizione_esame_corso
from django.db.models import Q

#funzione per creare l'iscrizione ad un esame di un corso
def add_iscrizone_esame_corso(id_stud,id_cors,id_esa):
     #iscrizione = Iscrizione_corso.objects.create(id_studente = id_studente, id_corso = id_corso)
     iscrizione =  Iscrizione_esame_corso(id_studente = id_stud, id_corso = id_cors, id_esame = id_esa)
     return "iscrizione all'esame avvenuto con successo."


#funzione per cancellare un'iscrizione ad un esame di un corso.
def del_iscrizone_esame_corso(id_stud,id_cors,id_esa):
     #prima verifico se lo studente è iscritto l corso

     iscrizione = Iscrizione_esame_corso.objects.filter(Q(id_studente = id_stud) & Q(id_corso = id_cors) & Q(id_esame = id_esa))
     iscrizione.delete()
     return "cancellazione con successo."


#funzione che dato uno studente ritorna tutte le sue iscrizioni
def lista_iscrizione_esame_studente(id_stud):
     return Iscrizione_esame_corso.objects.filter(id_studente = id_stud)


#funzione che dato un corso ritorna la lista di tutte le iscrizione all'esame di questo corso
def lista_iscriti_esame_corso(id_cors):
     return Iscrizione_esame_corso.objects.filter(id_corso = id_cors)


