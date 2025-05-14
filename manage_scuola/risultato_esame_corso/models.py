from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 

"""questo modello rappresenta i risultati degli esami.
e rappresentato dall id dello studente, l'id dell esame e il voto ottenuto all'esame."""

class Risultato_esame_corso(models.Model):
    #l'id viene generato automaticamente da django
    id_studente = models.IntegerField()
    id_corso = models.IntegerField()
    voto = models.IntegerField(validators=[
           MinValueValidator(0),  # Imposta il minimo a 0
            MaxValueValidator(30) # imposto il massimo a 30
    ])
    """queste funzioni agiscono sul singolo oggetto"""
    def get_id(self):
        return self.id
    
    def get_id_studente(self):
        return self.id_studente
    
    def get_id_corso(self):
        return self.id_corso
    
    def get_voto(self):
        return self.voto