from django.shortcuts import render , redirect
from .models import Iscrizione_corso
from django.db.models import Q
from corso.models import *
from corso.views import *
from  .forms import Iscrizione_corsoForm

# funzione per vedere la lista di tutte le iscrizioni
def list_iscrizioni(request):
   iscrizioni = Iscrizione_corso.objects.all()
   return render(request,'iscrizione_corso/lista_iscrizioni.html',{'iscrizioni':iscrizioni})


#funzione per aggiungere una nuova iscrizione
"""def add_iscrizione(id_stud,id_cors):
    iscrizione = Iscrizione_corso(id_studente = id_stud, id_corso = id_cors)
    iscrizione.save()
    #iscrizione = Iscrizione_corso.objects.create(id_studente = id_studente, id_corso = id_corso)
    return "iscrizione avvenuta con successo."""

def add_iscrizione(request):
    if request.method == 'POST':
        form = Iscrizione_corsoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iscrizioni')  # reindirizza dopo il salvataggio
    else:
        form = Iscrizione_corsoForm()
    return render(request, 'iscrizione_corso/add_iscrizione.html',{'form': form})


#funzione per ottenere la lista delle iscrizione dato l'id di uno studente
def lista_iscrizioni_studente(id):
    lista = Iscrizione_corso.objects.filter(id_studente = id) #ritorna lista iscrizioni dello studente
    lista_corsi=[]
    for i in lista:
        lista_corsi.append(get_corso(i.get_id_corso()).get_name())
    return lista_corsi



#funzione per cancellare un'iscrizione
def del_iscrizione(id_stud,id_cors):
    #studenti = Studente.objects.filter(Q(nome="Mario") | Q(cognome="Rossi"))
    iscrizione = Iscrizione_corso.objects.filter(Q(id_studente = id_stud) & Q(id_corso = id_cors))
    iscrizione.delete()

#funzione per ottenere un corso dato il suo id
"""def get_corso(id_corso):
   corso = Corso.objects.get(id=id_corso)  # Recupera lo studente con id = id_studente
   return corso  """ 
