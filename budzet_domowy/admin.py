# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Person
from .models import Kategoria

# Register your models here.

admin.site.register(Person)
admin.site.register(Kategoria)