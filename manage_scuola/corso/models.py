from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
"un corso è rappresentato da un codice univoco,il nome del corso, il codice(id)  del docente del corso, il codice(id) della sua categoria,il suo costo "

class Corso(models.Model):
    #l id viene gestito automaticamente da django
    name = models.CharField(max_length=255)
    id_docente = models.IntegerField()
    id_category = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)


