from django import forms 
from .models import Wydatki,Przychody

class WydatkiForm(forms.ModelForm):
    class Meta:
        model = Wydatki
        fields = [
            'kwota',
            'kategoria',
            'miesiac',
            'rok'
        ]

class PrzychodyForm(forms.ModelForm):
    class Meta:
        model = Przychody
        fields = [
            'nazwa_przychodu',
            'przychod',
            'miesiac',
            'rok'
            
            
        ]
        