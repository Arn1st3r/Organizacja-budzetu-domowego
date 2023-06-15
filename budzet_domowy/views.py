# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Person
from .models import Wydatki
from .fields import WydatkiForm

# Create your views here.
def wydatki_utworz_widok(request):
    form = WydatkiForm(request.POST or None)
    if form.is_valid():
        form.save(commit = True)
        form = WydatkiForm()
    context = {
        'form': form
    }
    return render(request, 'wydatki.html', context)


def statistics_view(request):
    liczba_osob = Person.objects.filter(imie="Julia").count()
    context = {
        'liczba_osob': liczba_osob
    }
    return render(request, 'index.html', context)


