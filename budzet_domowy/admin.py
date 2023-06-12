# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Person
from .models import Kategoria
from .models import Wydatki
from .models import Przychody
from .models import Cele
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    search_fields = ['imie', 'nazwisko', 'email']
    list_filter = ['imie', 'nazwisko']

class WydatkiAdmin(admin.ModelAdmin):
    search_fields = ['kwota', 'kategoria', 'osoba__imie']
    list_filter = ['kategoria']

admin.site.register(Person, PersonAdmin)
admin.site.register(Kategoria)
admin.site.register(Wydatki,WydatkiAdmin)
admin.site.register(Przychody)
admin.site.register(Cele)
