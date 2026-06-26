from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titolo', 'descrizione', 'luogo', 'data_ora', 'capienza_massima']
        widgets = {
            'data_ora': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-input'}),
            'titolo': forms.TextInput(attrs={'class': 'form-input'}),
            'descrizione': forms.Textarea(attrs={'class': 'form-input', 'rows': 4}),
            'luogo': forms.TextInput(attrs={'class': 'form-input'}),
            'capienza_massima': forms.NumberInput(attrs={'class': 'form-input'}),
        }