#formulario per add uno studente
from django import forms
from .models import Studente

class StudenteForm(forms.ModelForm):
    class Meta:
        model = Studente
        fields = ['name', 'surname', 'gender','birth']  # o '__all__' per tutti

        