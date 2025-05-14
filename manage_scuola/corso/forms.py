#form per aggiungere un nuovo corso

from django import forms
from .models import Corso

class CorsoForm(forms.ModelForm):
    class Meta:
        model = Corso
        fields = ['name', 'id_docente', 'cost']  # o '__all__' per tutti