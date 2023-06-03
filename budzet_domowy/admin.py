# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Person
from .models import Kategoria
from .models import Wydatki
from .models import Przychody
from .models import Cele
# Register your models here.

admin.site.register(Person)
admin.site.register(Kategoria)
admin.site.register(Wydatki)
admin.site.register(Przychody)
admin.site.register(Cele)
