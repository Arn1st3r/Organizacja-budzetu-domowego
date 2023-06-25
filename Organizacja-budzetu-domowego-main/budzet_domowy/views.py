# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Person
from .models import Wydatki,Kategoria, Przychody
from django.http import HttpResponse
from .fields import WydatkiForm, PrzychodyForm
from django.db.models import Sum


# Create your views here.
def przychody_view(request):
    form = PrzychodyForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        form = PrzychodyForm()
    context = {
        'form': form,
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

    context = {
        'form': form,
        'kwota_per_category': kwota_per_category_with_names,
    }
    return render(request, 'wydatki.html', context)


def statistics_view(request):
    context = {
        
    }
    return render(request, 'index.html', context)


