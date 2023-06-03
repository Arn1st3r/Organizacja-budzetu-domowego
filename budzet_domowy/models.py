# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Person(models.Model):
    imie = models.CharField(max_length=30, unique=True)
    nazwisko = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=250, blank=True)


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
    kategoria = models.CharField(max_length=30)
