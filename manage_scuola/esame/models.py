from django.db import models

"""questa rappresenta gli esami che vengno sreati nella scuola.
ogni esame e rappresentata da un id , l'id del  corso al quale si rifersice,il suo status( se è ancora possibile iscriversi (open) o no (close) a quel
esame)"""

class Esame(models.Model):
    id_corso = models.IntegerField()
    status = models.BooleanField(default=True)# True = iscrizione esame apertom False = iscrizione esame chiuso
