# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Person
from .models import Kategoria
from .models import Wydatki
from .models import Przychody, lista_lat, lista_miesiecy
from .models import Cele
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    search_fields = ['imie', 'nazwisko', 'email']
    list_filter = ['imie', 'nazwisko']

class WydatkiAdmin(admin.ModelAdmin):
    search_fields = ['kwota', 'kategoria', 'miesiac', 'rok']
    list_filter = ['kategoria','miesiac', 'rok']

class PrzychodyAdmin(admin.ModelAdmin):
    search_fields = ['nazwa_przychodu','miesiac', 'rok']
    list_filter = ['nazwa_przychodu', 'miesiac', 'rok']

admin.site.register(Person, PersonAdmin)
admin.site.register(lista_lat)
admin.site.register(lista_miesiecy)
admin.site.register(Kategoria)
admin.site.register(Wydatki,WydatkiAdmin)
admin.site.register(Przychody, PrzychodyAdmin)
admin.site.register(Cele)
