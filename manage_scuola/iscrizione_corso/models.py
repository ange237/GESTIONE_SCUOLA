from django.db import models

# Create your models here.
"""questo modello rappresenta la tabella iscrizione ad un corso. quando uno studente viene registratto come iscritto ad un determnato corso.
ed è rappresentato dall id dello studente, l id del corso. """

class Iscrizione_corso(models.Model):
    id_studente = models.IntegerField()
    id_corso = models.IntegerField()