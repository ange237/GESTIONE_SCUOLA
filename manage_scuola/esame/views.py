from django.shortcuts import render
from .models import Esame

#funzione per creare un esame
def add_esame(id_corso,status,description):
    Esame.objects.create(id_corso=id_corso, status = status, description = description)
    return "esame creato con successo."

#funzione per cancellare un esame
def del_esame(id_esame):
  esame = Esame.objects.get(id=id_esame)
  esame.delete()
  return "esame cancellato con successo."

#funzione che dato l'id di un esame ritorna le sue informazioni
def get_esame(id_esame):
   esame = Esame.objects.get(id=id_esame)
   return esame


#funzione per cambiare lo status di un esame
def change_status(id_esame,status):
   esame = Esame.objects.get(id=id_esame)
   esame.status = status
   return "cambiamento avvenuto con successo."


