#form per aggiungere un nuovo corso

from django import forms
from .models import Docente

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['name', 'surname', 'gender','birth','experience']  # o '__all__' per tutti