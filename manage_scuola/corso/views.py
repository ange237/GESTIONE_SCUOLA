from django.shortcuts import render , redirect
from .models import Corso
from  .forms import CorsoForm
from django.shortcuts import get_object_or_404, redirect


#funzione che ritorna tutti i corsi disponibile
def lista_corsi(request):
   corsi = Corso.objects.all()
   return render(request,'studente/lista_corsi.html',{'corsi':corsi})


#funzione per creare un nuovo corso
""""def add_corso(name,id_docente,costo):
    Corso.objects.create(name=name, id_docente= id_docente,costo = costo)
    return "corso creato con successo."""

def add_corso(request):
    if request.method == 'POST':
        form = CorsoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('corsi')  # reindirizza dopo il salvataggio
    else:
        form = CorsoForm()
    return render(request, 'corso/add_corso.html',{'form': form})



#funzione per cancellare un corso
"""def del_corso(id_corso):
  corso = Corso.objects.get(id=id_corso)
  corso.delete()
  return "corso cancellato con successo."""

def del_corso(request, id):
    corso = get_object_or_404(Corso, id=id)

    if request.method == 'POST':
        corso.delete()
        return redirect('corsi')  # Usa il name della URL della lista studenti

    # Se uno prova ad accedere via GET, reindirizzi alla lista (opzionale)
    return redirect('corsi')

#funzione per ottenere un corso dato il suo id
def get_corso(id_corso):
   corso = Corso.objects.get(id=id_corso)  
   return corso


#funzione che dato l'id di un docente ritorna i corsi a lui associati
def lista_corsi_doc(id):
   lista = Corso.objects.filter(id_docente = id)
   corsi =[]
   for i in lista:
      corsi.append(i.get_name())
   return corsi   

