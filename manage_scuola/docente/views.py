from django.shortcuts import render
from .models import Docente
from corso.views import *
from  .forms import DocenteForm

#funzione per ottenere la lista dei docenti
def lista_docenti(request):
    docenti = Docente.objects.all()
    return render(request,'studente/lista_docenti.html',{"docenti":docenti})



#funzione per aggiungere un nuovo docente
"""def add_docente(request,name,surname,gender,birth,experience):
    Docente.objects.create(name=name, surname=surname, gender =gender,birth =birth,experience = experience)
    return "docente aggiunto con successo"""

def add_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('docenti')  # reindirizza dopo il salvataggio
    else:
        form = DocenteForm()
    return render(request, 'docente/add_docente.html',{'form': form})



#funzion che dato l'id di un docente ritorna le informazioni a lui associati
def get_docente(id_docente):
   docente = Docente.objects.get(id=id_docente)  # Recupera lo studente con id = id_studente
   return docente


#funzione per cancellare uno docente
"""def del_docente(id_docente):
    docente =Docente.objects.get(id=id_docente)
    docente.delete()
    return "cancellazione con successo."""

def del_docente(request, id):
    docente = get_object_or_404(Docente, id=id)

    if request.method == 'POST':
        docente.delete()
        return redirect('docenti')  # Usa il name della URL della lista studenti

    # Se uno prova ad accedere via GET, reindirizzi alla lista (opzionale)
    return redirect('docenti')


#funzione che dato l'id di uno docente visualizza tutti i suoi corsi
def lista_corsi_docente(request,id):
    #interagira con la tabella corso
    docente = get_object_or_404(Docente, id=id)
    list = lista_corsi_doc(id)
    #return list
    return render(request,'docente/lista_corsi_docente.html',{'lista':list, 'nome':docente.get_name(),'matricola':docente.get_id() })


