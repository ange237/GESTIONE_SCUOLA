from django.db import models

# Create your models here.
"""questo modello rappresenta la tabella iscrizione ad un corso. quando uno studente viene registratto come iscritto ad un determnato corso.
ed è rappresentato dall id dello studente, l id del corso. """

class Iscrizione_corso(models.Model):
    #l'id viene generato automaticamente da django
    id_studente = models.IntegerField()
    id_corso = models.IntegerField()
    
    """queste funzioni agiscono sul singolo oggetto"""
    def get_id(self):
        return self.id
    
    def  get_id_studente(self):
        return self.id_studente
    
    def get_id_corso(self):
        return self.id_corso