# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(Slider)
