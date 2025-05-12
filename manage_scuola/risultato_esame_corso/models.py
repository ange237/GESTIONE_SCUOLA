from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 

"""questo modello rappresenta i risultati degli esami.
e rappresentato dall id dello studente, l'id dell esame e il voto ottenuto all'esame."""

class Risultato_esame_corso(models.Model):
    id_studente = models.IntegerField()
    id_esame = models.IntegerField()
    voto = models.IntegerField(validators=[
           MinValueValidator(0),  # Imposta il minimo a 0
            MaxValueValidator(30) # imposto il massimo a 30
        ])
