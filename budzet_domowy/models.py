# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Person(models.Model):
    imie = models.CharField(max_length=30, unique=True)
    nazwisko = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=250, blank=True)


    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    class Meta:
            verbose_name_plural = "Osoby"
class Kategoria(models.Model):
     nazwa = models.CharField(max_length=50, unique=True)
     opis = models.TextField(blank=True)

     class Meta:
          verbose_name_plural = "Kategorie"
    
     def __str__(self):
        return f"{self.nazwa}"
     
class Wydatki(models.Model):
    kwota = models.FloatField(unique=True)
    kategoria = models.OneToOneField(Kategoria, unique=True, null=True)
    Osoba = models.OneToOneField(Person, unique=True, null=True)

    def __str__(self):
        return f"{self.kwota} pln, {self.kategoria}"
     
    class Meta:
          verbose_name_plural = "Wydatki"

class Przychody(models.Model):
     nazwa_przychodu = models.CharField(max_length=100, unique=True)
     przychod = models.FloatField(unique=True)
     osoba = models.OneToOneField(Person, unique=True, null=True)
     data = models.DateField(unique=True, null=True)

     class Meta:
          verbose_name_plural = "Przychody"

     def __str__(self):
        return f"{self.nazwa_przychodu}, {self.osoba.imie}"