from django.db import models

"""questo modello rappresenta la tabella iscrizione ad un esame di un corso. quando uno studente viene registratto come iscritto ad unesame di un
 determnato corso.
ed è rappresentato dall id dello studente, l id del corso anziche l'id del esame al quale viene iscrito lo studente. """

class Iscrizione_esame_corso(models.Model):
    #l'id viene generato automaticamente da django
    #uno studente puo essere iscrito ad un solo esame di un determinato corso.
    id_studente =  models.IntegerField()
    id_corso = models.IntegerField()
    id_esame = models.IntegerField()