# -*- coding: utf-8 -*-
from django.db import models
from django.core import validators
from django.core.validators import MinValueValidator


class Person(models.Model):
    imie = models.CharField(max_length=30, blank=False, validators=[
        validators.MinLengthValidator(2, 'Imię powinno składać się przynajmniej z 2 znaków.'),validators.MaxLengthValidator(30, 'Imię może zawierać maksymalnie 30 znaków.')])
    nazwisko = models.CharField(max_length=30, blank=False,validators=[
        validators.MinLengthValidator(2, 'Nazwisko powinno składać się przynajmniej z 2 znaków.'),
        validators.MaxLengthValidator(30, 'Nazwisko może zawierać maksymalnie 30 znaków.')
    ])
    email = models.EmailField(max_length=250, blank=True, validators=[
        validators.EmailValidator('Podaj poprawny adres email.')
    ])

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    class Meta:
        verbose_name_plural = "Osoby"

class lista_miesiecy(models.Model):
    miesiac = models.CharField(max_length = 100, primary_key=True, blank=False)

    class Meta:
        verbose_name_plural = 'Miesiąc'
    
    def __str__(self):
        return f"{self.miesiac}"

class lista_lat(models.Model):
    rok = models.CharField(max_length = 4, primary_key=True, blank=False)

    class Meta:
        verbose_name_plural = 'Rok'
    
    def __str__(self):
        return f"{self.rok}"

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=50, blank=False, validators=[
        validators.MinLengthValidator(2, 'Nazwa kategorii powinna składać się przynajmniej z 2 znaków.'),validators.MaxLengthValidator(30, 'Nazwa kategorii może zawierać maksymalnie 50 znaków.')])
    opis = models.TextField(blank=True)
    class Meta:
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return f"{self.nazwa}"



class Wydatki(models.Model):
    kwota = models.FloatField(blank=False, validators=[
        MinValueValidator(0.0, 'Wartość musi być większa niż 0.')])
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, blank=False, default='')
    miesiac = models.ForeignKey(lista_miesiecy, on_delete=models.CASCADE, blank=False, default='')
    rok = models.ForeignKey(lista_lat, on_delete=models.CASCADE, blank=False, default='')
    
    def __str__(self):
        return f"{self.kwota} PLN, {self.kategoria}, {self.miesiac}-{self.rok}"

    class Meta:
        verbose_name_plural = "Wydatki"


class Przychody(models.Model):
    nazwa_przychodu = models.CharField(max_length=50, blank=False, validators=[
        validators.MinLengthValidator(2, 'Nazwa powinna składać się przynajmniej z 2 znaków.'),validators.MaxLengthValidator(50, 'Nazwa może zawierać maksymalnie 50 znaków.')])
    przychod = models.FloatField(blank=False, validators=[
        MinValueValidator(0.0, 'Wartość musi być większa niż 0.')])
    miesiac = models.ForeignKey(lista_miesiecy, on_delete=models.CASCADE, blank=False, default='')
    rok = models.ForeignKey(lista_lat, on_delete=models.CASCADE, blank=False, default='')

    class Meta:
        verbose_name_plural = "Przychody"

    def __str__(self):
        return f"{self.nazwa_przychodu} - {self.przychod} zł"



class Cele(models.Model):
    nazwa = models.CharField(max_length=50, blank=False, validators=[
        validators.MinLengthValidator(2, 'Nazwa powinna składać się przynajmniej z 2 znaków.'),validators.MaxLengthValidator(50, 'Nazwa może zawierać maksymalnie 50 znaków.')])
    kwota = models.FloatField(blank=False, validators=[
        MinValueValidator(0.0, 'Wartość musi być większa niż 0.')])
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Cele miesięczne"

    def __str__(self):
        return f"{self.nazwa}";
    

