from django import forms 
from .models import Wydatki

class WydatkiForm(forms.ModelForm):
    class Meta:
        model = Wydatki
        fields = [
            'kwota',
            'kategoria',
            
        ]