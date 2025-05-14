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
    experience = models.IntegerField(default=0)

    
    """queste funzioni agiscono sul singolo oggetto"""
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    
    def get_gender(self):
        return self.gender
    
    def get_birth(self):
        return self.gender
    
    def get_experience(self):
        return self.experience
