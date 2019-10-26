from django import forms
from .models import *

class GeneroForms(forms.ModelForm):
    class Meta:
        model = Genero
        fields=['title']
