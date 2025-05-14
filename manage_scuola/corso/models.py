from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
"un corso è rappresentato da un codice univoco,il nome del corso, il codice(id)  del docente del corso, il codice(id) della sua categoria,il suo costo "

class Corso(models.Model):
    #l id viene gestito automaticamente da django
    name = models.CharField(max_length=255)
    id_docente = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    """queste funzioni agiscono sul singolo oggetto"""
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_id_docente(self):
        return self.id_docente
    
    def get_cost(self):
        return self.cost
    


