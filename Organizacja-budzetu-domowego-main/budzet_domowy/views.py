# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .fields import WydatkiForm, PrzychodyForm
from django.db.models import Sum
from .models import Wydatki, Kategoria, Przychody


# Create your views here.
def przychody_view(request):
    form = PrzychodyForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        form = PrzychodyForm()
        #Wydobycie wartosci 'przychod' dla nazwy przychodu
    przychody_per_name = (
        Przychody.objects
        .values('nazwa_przychodu')
        .annotate(total_przychod=Sum('przychod'))
    )
        #Wydobycie wartosci 'przychod' dla miesiaca oraz kategorii
    przychody_per_month = (
        Przychody.objects
        .values('miesiac', 'rok')
        .annotate(total_przychod=Sum('przychod'))
    )

    context = {
        'form': form,
        'przychody_per_name': przychody_per_name,
        'przychody_per_month': przychody_per_month,
    }

    return render(request, 'przychody.html', context)

def wydatki_view(request):
    form = WydatkiForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        form = WydatkiForm()

    # Wydobycie wartości 'kwota' dla każdej kategorii
    kwota_per_category = (
        Wydatki.objects
        .values('kategoria')
        .annotate(total_kwota=Sum('kwota'))
    )

    # Mapowanie numeru kategorii na nazwę kategorii
    kwota_per_category_with_names = []
    for entry in kwota_per_category:
        category_id = entry['kategoria']
        category_name = Kategoria.objects.get(id=category_id).nazwa
        entry['kategoria'] = category_name
        kwota_per_category_with_names.append(entry)

    # Wydobycie wartości 'kwota' dla każdego miesiąca
    kwota_per_month = (
        Wydatki.objects
        .values('miesiac') 
        .annotate(total_kwota=Sum('kwota'))
    )

    context = {
        'form': form,
        'kwota_per_category': kwota_per_category_with_names,
        'kwota_per_month': kwota_per_month,
    }
    return render(request, 'wydatki.html', context)

def statistics_view(request):
    # Pobranie sumy przychodów dla każdego miesiąca
    przychody_per_month = (
        Przychody.objects
        .values('miesiac')
        .annotate(total_przychody=Sum('przychod'))
    )

    # Pobranie sumy wydatków dla każdego miesiąca
    wydatki_per_month = (
        Wydatki.objects
        .values('miesiac')
        .annotate(total_wydatki=Sum('kwota'))
    )

    # Obliczenie różnicy między przychodami a wydatkami dla każdego miesiąca
    roznica_per_month = []
    for przychod_entry in przychody_per_month:
        miesiac = przychod_entry['miesiac']
        przychod = przychod_entry['total_przychody'] or 0.0
        wydatki_entry = next((entry for entry in wydatki_per_month if entry['miesiac'] == miesiac), {})
        wydatki = wydatki_entry.get('total_wydatki', 0.0)
        roznica = przychod - wydatki
        roznica_per_month.append({'miesiac': miesiac, 'roznica': roznica})

    # Reszta kodu
    form = WydatkiForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        form = WydatkiForm()

    kwota_per_category = (
        Wydatki.objects
        .values('kategoria')
        .annotate(total_kwota=Sum('kwota'))
    )

    kwota_per_category_with_names = []
    for entry in kwota_per_category:
        category_id = entry['kategoria']
        category_name = Kategoria.objects.get(id=category_id).nazwa
        entry['kategoria'] = category_name
        kwota_per_category_with_names.append(entry)

    context = {
        'form': form,
        'kwota_per_category': kwota_per_category_with_names,
        'roznica_per_month': roznica_per_month,
    }
    return render(request, 'index.html', context)