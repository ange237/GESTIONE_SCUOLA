#formulario per add uno studente
from django import forms
from .models import Iscrizione_corso

class Iscrizione_corsoForm(forms.ModelForm):
    class Meta:
        model = Iscrizione_corso
        fields = ['id_studente', 'id_corso']  # o '__all__' per tutti