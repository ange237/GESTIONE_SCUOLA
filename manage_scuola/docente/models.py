from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
"il modello docente  rappresenta la tabella docente del nostro progetto."
"uno docente  è rappresentato dal suo id,nome, cognome,genere(M/F),data di nascita nel formato dd/mm/aaaa,anzianità(intero)"
""

class Docente(models.Model):
    #l id viene gestito automaticamente da django
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    gender = models.CharField(max_length=1,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(1)
        ])
    birth = models.DateField(null = True) # fomato data : YYYY-MM-DD
    experience = models.IntegerField()