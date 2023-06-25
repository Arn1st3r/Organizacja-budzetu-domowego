# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projekt.settings')
import django
django.setup()
import pytest
from django.core.validators import ValidationError
from .models import Person, lista_miesiecy, lista_lat, Kategoria, Wydatki, Przychody, Cele
from django.test import TransactionTestCase

class PersonTestCase(TransactionTestCase):
    def test_create_person(self):
        person = Person.objects.create(imie='Jan', nazwisko='Nowak', email='jan.nowak@example.com')
        self.assertEqual(person.imie, 'Jan')
        self.assertEqual(person.nazwisko, 'Nowak')
        self.assertEqual(person.email, 'jan.nowak@example.com')

    def test_get_person(self):
        person = Person(imie='Jan', nazwisko='Nowak', email='jan.nowak@example.com')
        self.assertEqual(person.imie, 'Jan')
        self.assertEqual(person.nazwisko, 'Nowak')
        self.assertEqual(person.email, 'jan.nowak@example.com')

class ListaMiesiecyTestCase(TransactionTestCase):
    def setUp(self):
        self.miesiac = lista_miesiecy.objects.create(miesiac='Styczeń')

    def test_lista_miesiecy_model(self):
        self.assertEqual(self.miesiac.miesiac, 'Styczeń')

class ListaLatTestCase(TransactionTestCase):
    def setUp(self):
        self.rok = lista_lat.objects.create(rok='2023')

    def test_lista_lat_model(self):
        self.assertEqual(self.rok.rok, '2023')

class KategoriaTestCase(TransactionTestCase):
    def setUp(self):
        self.kategoria = Kategoria.objects.create(nazwa='Jedzenie', opis='Opis kategorii')

    def test_kategoria_model(self):
        self.assertEqual(self.kategoria.nazwa, 'Jedzenie')
        self.assertEqual(self.kategoria.opis, 'Opis kategorii')

class WydatkiTestCase(TransactionTestCase):
    def setUp(self):
        self.kategoria = Kategoria.objects.create(nazwa='Jedzenie', opis='Opis kategorii')
        self.miesiac = lista_miesiecy.objects.create(miesiac='Styczeń')
        self.rok = lista_lat.objects.create(rok='2023')
        self.wydatki = Wydatki.objects.create(kwota=100.0, kategoria=self.kategoria, miesiac=self.miesiac, rok=self.rok)

    def test_wydatki_model(self):
        self.assertEqual(self.wydatki.kwota, 100.0)
        self.assertEqual(self.wydatki.kategoria, self.kategoria)
        self.assertEqual(self.wydatki.miesiac, self.miesiac)
        self.assertEqual(self.wydatki.rok, self.rok)

class PrzychodyTestCase(TransactionTestCase):
    def setUp(self):
        self.miesiac = lista_miesiecy.objects.create(miesiac='Styczeń')
        self.rok = lista_lat.objects.create(rok='2023')
        self.przychody = Przychody.objects.create(nazwa_przychodu='Wynagrodzenie', przychod=500.0, miesiac=self.miesiac, rok=self.rok)

    def test_przychody_model(self):
        self.assertEqual(self.przychody.nazwa_przychodu, 'Wynagrodzenie')
        self.assertEqual(self.przychody.przychod, 500.0)
        self.assertEqual(self.przychody.miesiac, self.miesiac)
        self.assertEqual(self.przychody.rok, self.rok)

class CeleTestCase(TransactionTestCase):
    def setUp(self):
        self.cele = Cele.objects.create(nazwa='Wakacje', kwota=2000.0, opis='Opis celu')

    def test_cele_model(self):
        self.assertEqual(self.cele.nazwa, 'Wakacje')
        self.assertEqual(self.cele.kwota, 2000.0)
        self.assertEqual(self.cele.opis, 'Opis celu')