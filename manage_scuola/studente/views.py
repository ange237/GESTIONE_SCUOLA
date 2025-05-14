from django.shortcuts import render , redirect
from  .models import Studente
from  .forms import StudenteForm
from iscrizione_corso.views import *
from iscrizione_esame_corso.views import *
from risultato_esame_corso.views import *
from django.shortcuts import get_object_or_404, redirect

def home(request):
   return render(request,'studente/home.html')

# funzione per vedere la lista di tutti gli studenti iscriti nella scuola
def student_list(request):
   studenti = Studente.objects.all()
   return render(request,'studente/lista_studenti.html',{'studenti':studenti})




#funzione per creare ed aggiungere un nuovo studente alla scuola
"""def add_studente(request,name:str,surname:str,gender:str,birth:str =""):
    # Creazione di un nuovo studente
    studente = Studente(name=name, surname=surname, gender =gender,birth =birth)
    studente.save()  # Salva nel database
    #studente = Studente.objects.create(name="Mario", surname="Rossi", gender ='M',birth = '1999-12-30')"""

def add_studente(request):
    if request.method == 'POST':
        form = StudenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studenti')  # reindirizza dopo il salvataggio
    else:
        form = StudenteForm()
    return render(request, 'studente/add_studente.html',{'form': form})


#funzione per rimuovere uno studente
#coinvolgera la tabella studente
"""def del_student(request,id_studente):
  studente = Studente.objects.get(id=id_studente)
  studente.delete()
  #return redirect('studenti')"""

def del_student(request, id):
    studente = get_object_or_404(Studente, id=id)

    if request.method == 'POST':
        studente.delete()
        return redirect('studenti')  # Usa il name della URL della lista studenti

    # Se uno prova ad accedere via GET, reindirizzi alla lista (opzionale)
    return redirect('studenti')


#funzione per iscrivere uno studente ad un corso
#coinvolger la tabella iscrizione corso
def iscrivi_corso(request,id_studente:int,id_corso:int):
   return add_iscrizione(id_studente,id_corso)




#funzione per iscrivere uno studente ad un esame
#coinvolgera la tabella iscrizione esame
"""def iscrivi_stud_esame(request,id_studente,id_esame,id_corso):
   return add_iscrizone_esame_corso(id_studente,id_corso,id_esame)"""


#funzione per vedere i corsi ai quali uno studente è iscritto
def viz_corsi_studente(request,id):
   #coinvolgera la tabella iscrizione corso
   studente = get_object_or_404(Studente, id=id)
   lista = lista_iscrizioni_studente(id)
   return render(request,'studente/lista_corsi_studente.html',{'lista':lista, 'nome':studente.get_name(),'matricola':studente.get_id() })



#funzione per  vedere gli esami al quale uno studente è iscrito
"""def viz_esami_studente(request,id_studente):
   #coinvolgera la tabella esame 
   return lista_iscrizione_esame_studente(id_studente)"""


#funzione per  elencare i voti di uno studente agli esami che ha superato
"""def viz_voti_studente(request,id_studente):
   #coinvolgera la tabella risultato
   map = lista_risultati_studente(id_studente)
   return map"""
    



#funzione per ottenere i dati di uno studente dato il suo id
#funzione interna al programma 
def get_studente(id_studente):
   studente = Studente.objects.get(id=id_studente)  # Recupera lo studente con id = id_studente
   return studente




