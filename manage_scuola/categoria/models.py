from django.db import models

# Create your models here.
"il modello categoria  rappresenta la tabella delle categorie dei corsi del nostro progetto."
"una categoria   è rappresentata dal suo id e dal suo nome,"
""

class Ctegoria(models.Model):
     #l id viene gestito automaticamente da django
     name = models.CharField(max_length=255)