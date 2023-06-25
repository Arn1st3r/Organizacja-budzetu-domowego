from django.db import models

class Person(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    email = models.EmailField(max_length=250, blank=True)

    def __str__(self):
        return f"{self.imie}"

    class Meta:
        verbose_name_plural = "Osoby"

class lista_miesiecy(models.Model):
    miesiac = models.CharField(max_length = 100, primary_key=True)

    class Meta:
        verbose_name_plural = 'Miesiąc'
    
    def __str__(self):
        return f"{self.miesiac}"

class lista_lat(models.Model):
    rok = models.CharField(max_length = 4, primary_key=True)

    class Meta:
        verbose_name_plural = 'Rok'
    
    def __str__(self):
        return f"{self.rok}"

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.TextField(blank=True)
    class Meta:
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return f"{self.nazwa}"



class Wydatki(models.Model):
    kwota = models.FloatField()
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, null=False)
    miesiac = models.ForeignKey(lista_miesiecy, on_delete=models.CASCADE, null=False, default='')
    rok = models.ForeignKey(lista_lat, on_delete=models.CASCADE, null=False, default='')
    
    def __str__(self):
        return f"{self.kwota} PLN, {self.kategoria}, {self.miesiac}-{self.rok}"

    class Meta:
        verbose_name_plural = "Wydatki"


class Przychody(models.Model):
    nazwa_przychodu = models.CharField(max_length=100, null=False)
    przychod = models.FloatField(null=False)
    miesiac = models.ForeignKey(lista_miesiecy, on_delete=models.CASCADE, null=False, default='')
    rok = models.ForeignKey(lista_lat, on_delete=models.CASCADE, null=False, default='')

    class Meta:
        verbose_name_plural = "Przychody"

    def __str__(self):
        return f"{self.nazwa_przychodu} - {self.przychod} zł"



class Cele(models.Model):
    nazwa = models.CharField(max_length=200)
    kwota = models.FloatField(null=False)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Cele miesięczne"

    def __str__(self):
        return f"{self.nazwa}";
    
