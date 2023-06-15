from django.db import models

class Person(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    email = models.EmailField(max_length=250, blank=True)

    def __str__(self):
        return f"{self.imie}"

    class Meta:
        verbose_name_plural = "Osoby"


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return f"{self.nazwa}"



class Wydatki(models.Model):
    kwota = models.FloatField()
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)



    def __str__(self):
        return f"{self.kwota} PLN, {self.kategoria}"

    class Meta:
        verbose_name_plural = "Wydatki"


class Przychody(models.Model):
    nazwa_przychodu = models.CharField(max_length=100, unique=True)
    przychod = models.FloatField(unique=True)
    osoba = models.OneToOneField(Person, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField(unique=True, null=True)

    class Meta:
        verbose_name_plural = "Przychody"

    def __str__(self):
        return f"{self.nazwa_przychodu}, {self.osoba.imie}"


class Cele(models.Model):
    nazwa = models.CharField(max_length=200, unique=True)
    kwota = models.FloatField(unique=True)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Cele miesięczne"
